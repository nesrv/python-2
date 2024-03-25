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


# ===================================
    

class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        return iter(x[self.column] for x in self.lst)
