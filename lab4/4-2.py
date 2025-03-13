def validate(*validators):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Проверяем каждый аргумент на соответствие своему валидатору
            for i, (arg, validator) in enumerate(zip(args, validators)):
                if not validator(arg):
                    print(f"Аргумент {i} не прошел валидацию: {arg}")
            # Если все аргументы прошли валидацию, вызываем исходную функцию
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Пример использования:
@validate(lambda x: x > 0, lambda y: isinstance(y, str) and y[0]=='h')
def my_function(x, y):
    print(f"x = {x}, y = {y}")

my_function(10, "hello")
my_function(10, "yello")  # Всё работает
my_function(-1, "hello")  # Вызовет ошибку: ValueError: Аргумент 0 не прошел валидацию: -1
my_function(10, 123)      # Вызовет ошибку: ValueError: Аргумент 1 не прошел валидацию: 123