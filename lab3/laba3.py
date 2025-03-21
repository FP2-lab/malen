def recursive_find(data, target):
    if isinstance(data, list):
        for index, value in enumerate(data):
            result = recursive_find(value, target)
            if result is not None:
                return result + 1
    else:
        if data == target:
            return 1
    return None

# Пример использования:
print(recursive_find([1, 2, [3, 4, [5, [6, []]]]], 4))  # Вернёт 4
print(recursive_find([1, 2, [3, 4, [5, [6, []]]]], 'spam'))  # Вернёт None
##//////////////////////////////////////////////////////////////////////////////////
def iterative_find(data, target):
    stack = [data]  # Храним кортеж (текущий список, плоский индекс)
    flat_index = 0  # Плоский индекс

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            # Если это список, добавляем его элементы в стек с обновлением индекса
            for item in current[::-1]:  # Обратный порядок для правильного обхода
                stack.extend(reversed(current))  # Обратный порядок для правильного обхода
        else:
            # Если текущий элемент - это искомый элемент
            if current == target:
                return flat_index  # Возвращаем индекс найденного элемента
            flat_index += 1  # Увеличиваем плоский индекс для следующего элемента

    return None  # Если элемент не найден

# Пример использования:
print(iterative_find([1, 2, [3, 4, [5, [6, []]]]], 4))  # Вернёт 3
print(iterative_find([1, 2, [3, 4, [5, [6, []]]]], 'spam'))  # Вернёт None
##//////////////////////////////////////////////////////////////////////////////////
##//////////////////////////////////////////////////////////////////////////////////
def calculate_recursive(k, a1, b1):
    # Базовые условия
    if k == 1:
        return a1, b1
    
    # Рекурсивные вызовы
    b_prev = b1  # Запоминаем предыдущее значение b
    a_prev = a1  # Запоминаем предыдущее значение a
    b_current = 2 * b_prev**2 + b_prev  # Вычисляем текущее значение b
    a_current = 2 * b_prev + a_prev  # Вычисляем текущее значение a
    
    return calculate_recursive(k - 1, a_current, b_current)

# Пример использования
k = 5  # Количество итераций
a1 = 1  # Начальное значение a
b1 = 2  # Начальное значение b
result_a, result_b = calculate_recursive(k, a1, b1)
print(f"Результаты: a = {result_a}, b = {result_b}")
##//////////////////////////////////////////////////////////////////////////////////
def calculate_iterative(k, a1, b1):
    a_current = a1
    b_current = b1

    for i in range(1, k + 1):  # Итерируем от 1 до k
        b_prev = b_current
        a_prev = a_current
        b_current = 2 * b_prev**2 + b_prev  # Вычисляем текущее значение b
        a_current = 2 * b_prev + a_prev  # Вычисляем текущее значение a
    
    return a_current, b_current

# Пример использования
k = 5  # Количество итераций
a1 = 1  # Начальное значение a
b1 = 2  # Начальное значение b

print(f"Результаты: a = {result_a}, b = {result_b}")