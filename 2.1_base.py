n = float(input("Введите число для поиска факториала: "))

def get_factorial(n):
    factorial = 1
    for i in range(1, int(n) + 1):
        factorial = factorial * i
    return factorial

print(get_factorial(n))