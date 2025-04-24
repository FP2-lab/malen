from .base_calculations import ClothingCalculator

class Jacket(ClothingCalculator):
    """Класс для расчета пиджака"""
    
    def __init__(self):
        super().__init__("Пиджак")
        self._base_fabric = 1.5  # базовый расход ткани в метрах
    
    def calculate_fabric(self, size):
        """Рассчитывает расход ткани в зависимости от размера"""
        if size < 42 or size > 62:
            raise ValueError("Размер пиджака должен быть между 42 и 62")
        
        # Расчет ткани: база + 0.1м на каждый размер выше 46
        fabric = self._base_fabric + max(0, (size - 46) * 0.1)
        self._history.append(f"Расчет ткани для размера {size}: {fabric:.2f}м")
        return round(fabric, 2)
    
    def calculate_cost(self, size):
        """Рассчитывает стоимость пошива"""
        fabric = self.calculate_fabric(size)
        labor_cost = 2000 + (size - 42) * 100  # Чем больше размер, тем сложнее пошив
        total_cost = fabric * self.fabric_price + self.accessories_price + labor_cost
        
        self._history.append(
            f"Стоимость пошива для размера {size}: "
            f"{total_cost:.2f} руб (ткань: {fabric * self.fabric_price:.2f}, "
            f"фурнитура: {self.accessories_price:.2f}, работа: {labor_cost:.2f})"
        )
        return round(total_cost, 2)
    
    def __add__(self, other):
        """Комбинирование с брюками для получения костюма"""
        if isinstance(other, Pants):
            return ThreePieceSuit() 
        raise TypeError("Можно комбинировать только с брюками")

class Pants(ClothingCalculator):
    """Класс для расчета брюк"""
    
    def __init__(self):
        super().__init__("Брюки")
        self._base_fabric = 1.2
    
    def calculate_fabric(self, size):
        if size < 40 or size > 60:
            raise ValueError("Размер брюк должен быть между 40 и 60")
        
        fabric = self._base_fabric + max(0, (size - 44) * 0.08)
        self._history.append(f"Расчет ткани для размера {size}: {fabric:.2f}м")
        return round(fabric, 2)
    
    def calculate_cost(self, size):
        fabric = self.calculate_fabric(size)
        labor_cost = 1500 + (size - 40) * 80
        total_cost = fabric * self.fabric_price + self.accessories_price + labor_cost
        
        self._history.append(
            f"Стоимость пошива для размера {size}: "
            f"{total_cost:.2f} руб (ткань: {fabric * self.fabric_price:.2f}, "
            f"фурнитура: {self.accessories_price:.2f}, работа: {labor_cost:.2f})"
        )
        return round(total_cost, 2)

class ThreePieceSuit(ClothingCalculator):
    """Класс для расчета костюма-тройки (пиджак + брюки + жилет)"""
    
    def __init__(self):
        super().__init__("Костюм-тройка")
        self._jacket = Jacket()
        self._pants = Pants()
        self._vest_fabric = 0.8
    
    def calculate_fabric(self, size):
        jacket_fabric = self._jacket.calculate_fabric(size)
        pants_fabric = self._pants.calculate_fabric(size)
        total_fabric = jacket_fabric + pants_fabric + self._vest_fabric
        
        self._history.append(
            f"Общий расход ткани для костюма размера {size}: "
            f"{total_fabric:.2f}м (пиджак: {jacket_fabric:.2f}, "
            f"брюки: {pants_fabric:.2f}, жилет: {self._vest_fabric:.2f})"
        )
        return round(total_fabric, 2)
    
    def calculate_cost(self, size):
        jacket_cost = self._jacket.calculate_cost(size) - self._jacket.accessories_price
        pants_cost = self._pants.calculate_cost(size) - self._pants.accessories_price
        vest_cost = self._vest_fabric * self.fabric_price + 1000  # работа по жилету
        
        total_cost = jacket_cost + pants_cost + vest_cost + self.accessories_price
        discount = total_cost * 0.1  # скидка 10% на комплект
        
        self._history.append(
            f"Стоимость пошива костюма размера {size}: "
            f"{total_cost - discount:.2f} руб (с учетом скидки 10%)"
        )
        return round(total_cost - discount, 2)
    
    def __mul__(self, quantity):
        """Расчет оптовой скидки"""
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Количество должно быть положительным целым числом")
        
        if quantity >= 10:
            return quantity, 0.15  # 15% скидка за 10+ штук
        elif quantity >= 5:
            return quantity, 0.1  # 10% скидка за 5+ штук
        return quantity, 0
    