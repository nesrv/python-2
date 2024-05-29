class Record:

    def __init__(self, **kwargs):       
        self.__dict__.update(kwargs)       
        self._len = len(kwargs)
        self._keys = tuple(kwargs.keys())
       

    def __getitem__(self, item):
        return getattr(self, self._keys[item])

    def __setitem__(self, key, value):
        setattr(self, self._keys[key], value)


r = Record(pk=1, title='Python-2', author='Серов')

print(r)
r[1] = 4
print(r[1])

class Track:

    def __init__(self, start_x, start_y):
        self.N = []
        self.start_x = start_x
        self.start_y = start_y
        # self.N.append([self.start_x, self.start_y])

    def add_point(self, x, y, speed):
        self.N.append([x, y, speed])

    def __getitem__(self, item):
        if item > (len(self.N) - 1) or type(item) != int:
            raise IndexError('некорректный индекс')
        return tuple(self.N[item][:2]), self.N[item][2]

    def __setitem__(self, key, value):
        if key > len(self.N) - 1 or type(key) != int:
            raise IndexError('некорректный индекс')
        self.N[key][2] = value
