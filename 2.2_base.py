input = input("Введите числа через пробел: ")
numbers = []
current_number = ""

for char in input:
    if char == " ":
        if current_number != "":
            numbers.append(int(current_number))
            current_number = ""
    else:
        current_number += char

if current_number != "":
    numbers.append(int(current_number))

min = numbers[0]
for number in numbers:
    if number < min:
        min = number

print("Минимальный элемент:", min)