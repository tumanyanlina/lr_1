def word_counter(file_name: str):
    with open(file_name, 'r', encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        return "Ошибка: файл пуст"

    for char in "(),.!?;:-—\n":
        content = content.replace(char, " ")

    content = content.lower()
    words = content.split()

    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    return counter


file_path = r'c:\Users\tuman\OneDrive\Desktop\МиТП_лабы\python\file.txt'
result = word_counter(file_path)

if isinstance(result, dict):
    print("Частота слов в файле:", result)
else:
    print(result)
