import os

class File:
    def __init__(self, filename):
        self.filename = os.path.join("C:\\Users\\tuman\\OneDrive\\Desktop\\МиТП_лабы\\python", filename)
    
    def write(self, text):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Файл успешно создан.")
    
    def read(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "Ошибка: файл не найден."

file = File("f.txt")
file.write("1 2 3 4 5")
    
reading = file.read()
print("Содержимое файла:", reading)