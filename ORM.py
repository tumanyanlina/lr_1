class Table:
    def __init__(self):
        self.data = []

    def insert(self, book: dict):
        self.data.append(book)

    def select(self, **conditions):
        result = []
        for row in self.data:
            if all(row.get(key) == value for key, value in conditions.items()):
                result.append(row)
        return result


books = Table()
books.insert({"id": 1, "title": "Мастер и Маргарита", "author": "М.В.Булгаков"})
books.insert({"id": 2, "title": "Преступление и наказание", "author": "Ф.М.Достоевский"})
books.insert({"id": 2, "title": "Тихий Дон", "author": "М.А.Шолохов"})

print(books.select(id=1))
