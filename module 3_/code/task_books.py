class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __repr__(self):
        return f'Книга: "{self.name}" автор: {self.author}'

    def __hash__(self):
        return hash((self.name, self.author))

    def __eq__(self,other):
        return self.__hash__() == other.__hash__()

text = """Отцы и дети; Тургенев; 2024
Война и мир; Толстой; 2001
Братья Карамазовы; Достоевский; 1954
Война и мир; Толстой; 2022
Братья Карамазовы; Достоевский; 2024
Война и мир; Толстой; 1972"""

lst_in = text.splitlines()
lst_bs = []

for line in lst_in:
    line = line.split('; ')
    name, author, year = line
    book = BookStudy(name, author, year)
    lst_bs.append(book)


unique_books = set(lst_bs)
print(*unique_books, sep="\n")