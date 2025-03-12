def make_accumulator():
    collection = []  # Коллекция для накопления аргументов

    def accumulator(value):
        if value is None:  # Если получено определённое значение (например, None)
            result = collection.copy()   # Возвращаем копию коллекции
            collection.clear()  # Очищаем коллекцию
            return result
        else:
            collection.append(value)  # Добавляем аргумент в коллекцию
            return None  # Пока не достигнуто определённое значение, возвращаем None

    return accumulator

# Пример использования:
acc = make_accumulator()
acc(1)
acc(2)
acc(3)
print(acc(None))  # Вывод: [1, 2, 3]
acc(4)
print(acc(None))  # Вывод: [4]
acc(7)
print(acc(None))