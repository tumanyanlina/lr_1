try:
    text = input("Enter numbers: ")
    numbers = []
    current_number = ""
    
    for char in text:
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
            
    print("Min value:", min)
    
except ValueError:
    print("Error: Please enter numbers only!")
