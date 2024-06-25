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


# -----------------------------------------------------

class IterColumn:
    def __init__(self, lst, column):
        self.__column = list(zip(*lst))[column]

    def __iter__(self):
        return (x for x in self.__column)