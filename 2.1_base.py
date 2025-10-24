try:
    n = float(input("Введите число для поиска факториала: "))

    def get_factorial(n):
        if n != int(n):
            return "Ошибка: введите целое число."

        if n < 0:
            return "Ошибка: факториал отрицательных чисел не вычисляется."

        factorial = 1
        for i in range(1, int(n) + 1):
            factorial = factorial * i
        return factorial

    print(get_factorial(n))
except ValueError:
    print("Ошибка: вы ввели не число.")
