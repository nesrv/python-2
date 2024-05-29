class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([(x, y), speed])

    def __check(self, idx):
        if type(idx) != int or idx not in range(len(self.points)):
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        self.__check(key)
        self.points[key][1] = value

    def __getitem__(self, item):
        self.__check(item)
        return self.points[item]