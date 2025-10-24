text = input("Введите строку для подсчёта гласных: ")

if text == "":
    print("Ошибка: пустая строка.")
else:
    for char in text:
        if char in "0123456789":
            print("Ошибка: нельзя вводить цифры.")
            break
    else:
        count = 0
        for char in text.lower():
            if char in "аеёиоуыэюяaeiou":
                count += 1
        print("Количество гласных:", count)
