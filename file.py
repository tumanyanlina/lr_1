# file.py - простой калькулятор

def add_numbers(a, b):
    """Складывает два числа"""
    return a + b

def multiply_numbers(a, b):
    """Умножает два числа"""
    return a * b

# Пример использования
if __name__ == "__main__":
    x = 10
    y = 5
    
    result_add = add_numbers(x, y)
    result_multiply = multiply_numbers(x, y)
    
    print(f"Сложение: {x} + {y} = {result_add}")
    print(f"Умножение: {x} * {y} = {result_multiply}")
