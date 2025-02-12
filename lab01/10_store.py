#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
chair_code = goods['Стул']
table_code = goods['Стол']
sofa_code = goods['Диван']
print(f'цена лампы', store[lamp_code][0]['price'])
print()
print('склад 1 - цена стола', store[table_code][0]['price'])
print('склад 2 - цена стола', store[table_code][1]['price'])
print()
print('склад 1 - цена Диван', store[sofa_code][0]['price'])
print('склад 2 - цена Диван', store[sofa_code][1]['price'])
print()
print('склад 1 - цена Стул', store[chair_code][0]['price'])
print('склад 2 - цена Стул', store[chair_code][1]['price'])
print('склад 3 - цена Стул', store[chair_code][2]['price'])
print()
print('склад 1 - кол-во столов', store[table_code][0]['quantity'])
print('склад 2 - кол-во столов', store[table_code][1]['quantity'])

print('склад 1 - цена всех столов', store[table_code][0]['quantity'] * store[table_code][0]['price'])
print('склад 2 - цена всех столов', store[table_code][1]['quantity'] * store[table_code][1]['price'])
print('всего - цена всех столов', store[table_code][0]['quantity'] * store[table_code][0]['price'] + store[table_code][1]['quantity'] * store[table_code][1]['price'] )

print('склад 1 - кол-во стульев', store[chair_code][0]['quantity'])
print('склад 2 - кол-во стульев', store[chair_code][1]['quantity'])
print('склад 2 - кол-во стульев', store[chair_code][2]['quantity'])

print('склад 1 - цена всех стульев', store[chair_code][0]['quantity'] * store[chair_code][0]['price'])
print('склад 2 - цена всех стульев', store[chair_code][1]['quantity'] * store[chair_code][1]['price'])
print('склад 3 - цена всех стульев', store[chair_code][2]['quantity'] * store[chair_code][2]['price'])
print('всего - цена всех стульев', store[chair_code][0]['quantity'] * store[chair_code][0]['price'] + store[chair_code][1]['quantity'] * store[chair_code][1]['price'] + store[chair_code][2]['quantity'] * store[chair_code][2]['price']  )
