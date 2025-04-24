from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from clothing_calculator.utils import save_to_excel
from clothing_calculator.clothing_items import Jacket, Pants, ThreePieceSuit
from datetime import datetime
import os
from abc import ABC, abstractmethod
Window.size = (800, 600)

class ClothingTab(BoxLayout):
    """Базовый класс для вкладок расчета одежды"""
    
    def __init__(self, clothing_item, **kwargs):
        super().__init__(**kwargs)
        self.clothing_item = clothing_item
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # Цены
        price_layout = BoxLayout(size_hint_y=None, height=40)
        price_layout.add_widget(Label(text="Цена ткани за метр:"))
        self.fabric_price_input = TextInput(text="500", input_filter='float')
        price_layout.add_widget(self.fabric_price_input)
        
        price_layout.add_widget(Label(text="Цена фурнитуры:"))
        self.accessories_price_input = TextInput(text="300", input_filter='float')
        price_layout.add_widget(self.accessories_price_input)
        self.add_widget(price_layout)
        
        # Размер
        size_layout = BoxLayout(size_hint_y=None, height=40)
        size_layout.add_widget(Label(text="Размер:"))
        self.size_input = TextInput(text="48", input_filter='int')
        size_layout.add_widget(self.size_input)
        self.add_widget(size_layout)
        
        # Результаты
        self.result_layout = BoxLayout(orientation='vertical', size_hint_y=0.3)
        self.fabric_label = Label(text="Расход ткани: ")
        self.cost_label = Label(text="Стоимость пошива: ")
        self.result_layout.add_widget(self.fabric_label)
        self.result_layout.add_widget(self.cost_label)
        self.add_widget(self.result_layout)
        
        # История
        history_scroll = ScrollView()
        self.history_label = Label(text="История расчетов:\n", size_hint_y=None)
        self.history_label.bind(texture_size=self.history_label.setter('size'))
        history_scroll.add_widget(self.history_label)
        self.add_widget(history_scroll)
        
        # Кнопки
        btn_layout = BoxLayout(size_hint_y=None, height=40)
        calc_btn = Button(text="Рассчитать")
        calc_btn.bind(on_press=self.calculate)
        btn_layout.add_widget(calc_btn)
        
        export_btn = Button(text="Экспорт в Excel")
        export_btn.bind(on_press=self.export)
        btn_layout.add_widget(export_btn)
        
        clear_btn = Button(text="Очистить")
        clear_btn.bind(on_press=self.clear)
        btn_layout.add_widget(clear_btn)
        
        self.add_widget(btn_layout)
    
    def update_prices(self):
        """Обновляет цены ткани и фурнитуры"""
        try:
            self.clothing_item.fabric_price = float(self.fabric_price_input.text)
            self.clothing_item.accessories_price = float(self.accessories_price_input.text)
        except ValueError as e:
            self.show_popup("Ошибка", f"Некорректное значение цены: {str(e)}")
    
    def calculate(self, instance):
        """Выполняет расчет"""
        try:
            self.update_prices()
            size = int(self.size_input.text)
            
            fabric = self.clothing_item.calculate_fabric(size)
            cost = self.clothing_item.calculate_cost(size)
            
            self.fabric_label.text = f"Расход ткани: {fabric} м"
            self.cost_label.text = f"Стоимость пошива: {cost} руб"
            self.update_history()
        except ValueError as e:
            self.show_popup("Ошибка", str(e))
    
    def update_history(self):
        """Обновляет историю расчетов"""
        self.history_label.text = "История расчетов:\n" + "\n".join(
            self.clothing_item.history[-10:][::-1]
        )
    
    def export(self, instance):
        """Экспортирует данные в Excel"""
        try:
            data = []
            for record in self.clothing_item.history:
                if "ткани" in record:
                    parts = record.split(":")
                    data.append({
                        "type": self.clothing_item.name,
                        "size": parts[0].split()[-1],
                        "fabric": parts[1].strip().split()[0],
                        "details": record
                    })
                elif "Стоимость" in record:
                    parts = record.split(":")
                    data.append({
                        "type": self.clothing_item.name,
                        "size": parts[0].split()[-1],
                        "cost": parts[1].strip().split()[0],
                        "details": record
                    })
            
            if data:
                filename = save_to_excel(data)
                self.show_popup("Успех", f"Данные экспортированы в {os.path.abspath(filename)}")
            else:
                self.show_popup("Информация", "Нет данных для экспорта")
        except Exception as e:
            self.show_popup("Ошибка", f"Ошибка экспорта: {str(e)}")
    
    def clear(self, instance):
        """Очищает историю"""
        self.clothing_item._history.clear()
        self.history_label.text = "История расчетов:\n"
        self.fabric_label.text = "Расход ткани: "
        self.cost_label.text = "Стоимость пошива: "
    
    def show_popup(self, title, message):
        """Показывает всплывающее окно"""
        popup = Popup(title=title, size_hint=(0.8, 0.4))
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        btn = Button(text="OK", size_hint_y=None, height=40)
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.content = content
        popup.open()

class JacketTab(ClothingTab):
    def __init__(self, **kwargs):
        super().__init__(Jacket(), **kwargs)

class PantsTab(ClothingTab):
    def __init__(self, **kwargs):
        super().__init__(Pants(), **kwargs)

class SuitTab(ClothingTab):
    def __init__(self, **kwargs):
        super().__init__(ThreePieceSuit(), **kwargs)
        
        # Добавляем поле для количества (оптовая скидка)
        quantity_layout = BoxLayout(size_hint_y=None, height=40)
        quantity_layout.add_widget(Label(text="Количество (для опта):"))
        self.quantity_input = TextInput(text="1", input_filter='int')
        quantity_layout.add_widget(self.quantity_input)
        self.add_widget(quantity_layout)
        
        # Перемещаем результат ниже
        self.remove_widget(self.result_layout)
        self.add_widget(self.result_layout)
    
    def calculate(self, instance):
        """Расчет с учетом оптовой скидки"""
        try:
            self.update_prices()
            size = int(self.size_input.text)
            quantity = int(self.quantity_input.text)
            
            fabric = self.clothing_item.calculate_fabric(size)
            base_cost = self.clothing_item.calculate_cost(size)
            
            qty, discount = self.clothing_item * quantity
            total_cost = base_cost * qty * (1 - discount)
            
            quantity, discount = self.clothing_item  * 7
            print(f"Заказ {quantity} шт. Скидка: {discount*100}%")  
            self.fabric_label.text = f"Расход ткани: {fabric} м"
            if discount > 0:
                self.cost_label.text = (
                    f"Стоимость {qty} шт: {total_cost:.2f} руб "
                    f"(скидка {discount*100:.0f}%)"
                )
            else:
                self.cost_label.text = f"Стоимость пошива: {base_cost} руб"
            
            self.update_history()
        except ValueError as e:
            self.show_popup("Ошибка", str(e))

class ClothingApp(App):
    def build(self):
        self.title = "Ателье - расчет одежды"
        
        tab_panel = TabbedPanel(do_default_tab=False)
        
        jacket_tab = TabbedPanelItem(text='Пиджак')
        jacket_tab.add_widget(JacketTab())
        tab_panel.add_widget(jacket_tab)
        
        pants_tab = TabbedPanelItem(text='Брюки')
        pants_tab.add_widget(PantsTab())
        tab_panel.add_widget(pants_tab)
        
        suit_tab = TabbedPanelItem(text='Костюм-тройка')
        suit_tab.add_widget(SuitTab())
        tab_panel.add_widget(suit_tab)
        
        return tab_panel

if __name__ == '__main__':
    ClothingApp().run()

class Shape(ABC):
    pass
why= Shape()

suit = ThreePieceSuit()
print(suit * 3)


jacket = Jacket()
jacket.fabric_price = 500 
##jacket.accessories_price = 300  
##print(jacket.fabric_price) 
##print(jacket.accessories_price) 
print(jacket.name)