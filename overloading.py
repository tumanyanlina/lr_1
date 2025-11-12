class Box:
    def __init__(self, stuff):
        self.stuff = stuff
    
    def __add__(self, other):
        return Box(self.stuff + other.stuff)
    
    def __str__(self):
        return ", ".join(self.stuff)
        
Box_1 = Box(["Книга", "ручка", "часы", "степлер"])
Box_2 = Box(["компьютерная мышь", "планшет", "фотоаппарат"])
Box_3 = Box_1 + Box_2
print(Box_3)
    