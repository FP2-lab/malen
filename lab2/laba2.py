from itertools import product

# Задача 1: Сколько различных кодов может составить Иван?
def count_codes():
    """
    Возвращает количество 5-буквенных кодов, которые можно составить из букв И, В, А, Н,
    используя каждую букву хотя бы один раз.

    >>> count_codes()
    781
    """
    letters = ['И', 'В', 'А', 'Н']
    total_codes = len(letters) ** 5  # Общее количество кодов
    codes_without_I = (len(letters) - 1) ** 5  # Количество кодов без буквы И
    codes_with_I = total_codes - codes_without_I  # Количество кодов с буквой И
    return codes_with_I

# Задача 2: Значение арифметического выражения
def compute_expression():
    """
    Вычисляет значение арифметического выражения 7 * 512 - 6 * 64 + 8 * 210 - 255.

    >>> compute_expression()
        
    """
    result = 7 * 512 - 6 * 64 + 8 * 210 - 255
    return result

def convert_to_octal(n):
    """
    Преобразует число n в восьмеричную систему счисления.

    >>> convert_to_octal(10)
    '12'
    >>> convert_to_octal(128)
    '200'
    """
    octal_value = ''
    while n > 0:
        octal_value = str(n % 8) + octal_value
        n //= 8
    return octal_value

def count_zeros_in_octal(n):
    """
    Возвращает количество цифр 0 в восьмеричном представлении числа n.

    >>> count_zeros_in_octal(10)
    0
    >>> count_zeros_in_octal(128)
    2
    """
    octal_value = convert_to_octal(n)
    return octal_value.count('0')

# Задача 3: Найти число с максимальным количеством делителей в заданном диапазоне
def count_divisors(n):
    """
    Возвращает количество натуральных делителей числа n.

    >>> count_divisors(6)
    4
    >>> count_divisors(12)
    6
    """
    count = 0
    for i in range(1, int(n)+1):
        if n % i == 0:
            count += 1
            
    return count

def max_divisors_in_range(start, end):
    """
    Возвращает число с максимальным количеством делителей в диапазоне [start, end].

    >>> max_divisors_in_range(2, 48)
    (10, 48)
    >>> max_divisors_in_range(84052, 84130)
    (72, 84096)
    """
    max_divisors = 0
    number_with_max_divisors = start
    for number in range(start, end + 1):
        divisors = count_divisors(number)
        if divisors > max_divisors:
            max_divisors = divisors
            number_with_max_divisors = number
    return max_divisors, number_with_max_divisors

# Выполнение задач
if __name__ == "__main__":
    # Задача 1
    num_codes = count_codes()
    print("Количество кодов (Задача 1):", num_codes)

    # Задача 2
    result = compute_expression()
    zeros_count = count_zeros_in_octal(result)
    print("Результат выражения (Задача 2):", result)
    print("Количество цифр 0 в восьмеричном представлении:", zeros_count)

    # Задача 3
    max_div_count, number = max_divisors_in_range(84052, 84130)
    print("Максимальное количество делителей:", max_div_count)
    print("Число с максимально большим количеством делителей:", number)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
