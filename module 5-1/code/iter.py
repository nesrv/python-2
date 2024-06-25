class IterColumn:

    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.value = -1
        return self

    def __next__(self):
        if self.value < 3:
            self.value += 1
            return self.lst[self.value][self.column]
        else:
            raise StopIteration

# =======================================
        

class IterColumn:
    def __init__(self, lst, col):
        self.lst = lst
        self.col = col

    def __iter__(self):
        self.a = list(zip(*self.lst))
        return iter(self.a[self.col])

# ====================================
    

class IterColumn:
    def __init__(self, lst, column):
        self.lst, self.column = [lst[i][column]
                                 for i in range(len(lst))], column

    def __iter__(self):
        return iter(self.lst)


lst = [[11, 12, 13],
       [21, 22, 23],
       [31, 32, 33]
       ]

iter_matrix = IterColumn(lst, 2)


for x in iter_matrix:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)


# ===================================
    

class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        return iter(x[self.column] for x in self.lst)



# ========================================
    

class Cell:

    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:

    def __init__(self, rows, cols, type=int):
        self.__type = type
        self.__rows = rows
        self.__cols = cols
        self.__cells = tuple(tuple(Cell() for _ in range(cols))
                             for _ in range(rows))

    def __check_index(self, index):
        r, c = index
        if not (0 <= r < self.__rows) or not (0 <= c < self.__cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.__cells[r][c].data

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != self.__type:
            raise TypeError('неверный тип присваивания данных')
        r, c = key
        self.__cells[r][c].data = value

    def __iter__(self):
        for row in self.__cells:
            yield (x.data for x in row)
