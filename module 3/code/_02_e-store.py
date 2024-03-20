class Thing:
    i = 0

    def __init__(self, name, price):
        Thing.i += 1
        self.id = self.i
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    def get_data(self):
        return tuple(self.__dict__.values())


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):

    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


# или так

class Thing:
    id = 0

    def __init__(self, *args):
        self.id = Thing.id
        self.name, self.price, self.weight, self.dims, self.memory, self.frm = args
        Thing.id += 1

    def get_data(self):
        return tuple(self.__dict__.values())


class Table(Thing):

    def __init__(self, name, price, weight, dims, memory=None, frm=None):
        super().__init__(name, price, weight, dims, memory, frm)


class ElBook(Thing):

    def __init__(self, name, price, memory, frm, weight=None, dims=None):
        super().__init__(name, price, weight, dims, memory, frm)
