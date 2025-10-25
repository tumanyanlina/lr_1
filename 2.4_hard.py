import random
print("Я загадал число от 1 до 50. Угадайте его")
n = random.randint(1, 50)

while True:
    try:
        guess = int(input("Ваша догадка: "))
        if guess < n:
            print("Загаданное число больше.")
        elif guess > n:
            print("Загаданное число меньше.")
        else:
            print("Ура! Вы угадали!")
            break
    except ValueError:
        print("Пожалуйста, вводите только числа!")
