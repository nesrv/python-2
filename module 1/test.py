class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Александр Пушкин"
    views = 14356
    comments = 12

book1 = DataBase()
book2 = DataBase()
print(book1.__dict__)
print(book1.__dict__)
book2.title="123"
print(book1.__dict__)
print(book1.title)
print(book2.title)

