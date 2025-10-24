text = input("Введите строку для подсчёта гласных: ")
count = 0

for char in text.lower():
    if char in 'уеэёоаыяиюeyioa':
        count += 1

print("Количество гласных:", count)
