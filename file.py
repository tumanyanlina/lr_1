def add_numbers(a, b):
    """Складывает два числа"""
    return a + b


def multiply_numbers(a, b):
    """Умножает два числа"""
    return a * b


def subtract_numbers(a, b):
    """Вычитает два числа - НОВАЯ ФУНКЦИЯ"""
    return a - b


def divide_numbers(a, b):
    """Делит два числа - НОВАЯ ФУНКЦИЯ ДЕЛЕНИЯ"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b


def power_numbers(a, b):
    """Возводит a в степень b - НОВАЯ ФУНКЦИЯ СТЕПЕНИ"""
    return a ** b


# Пример использования
if __name__ == "__main__":
    x = 15
    y = 20
    z = 5  # Новое число для демонстрации

    result_add = add_numbers(x, y)
    result_multiply = multiply_numbers(x, y)
    result_subtract = subtract_numbers(x, y)
    result_divide = divide_numbers(x, z)
    result_power = power_numbers(x, z)

    print(f"Сложение: {x} + {y} = {result_add}")
    print(f"Умножение: {x} * {y} = {result_multiply}")
    print(f"Вычитание: {x} - {y} = {result_subtract}")
    print(f"Деление: {x} / {z} = {result_divide}")
    print(f"Степень: {x} ^ {z} = {result_power}")

    