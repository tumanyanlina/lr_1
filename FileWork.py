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
    def append(self):
        with open(self.filename, 'a', encoding='utf-8') as f:
           f.write("\n5 4 3 2 1")

file = File("f.txt")

file.write("1 2 3 4 5")    
content = file.read()
print("Исходное содержимое файла:")
print(content)

file.append()
new_content = file.read()
print("Обновленное содержимое файла:")
print(new_content)