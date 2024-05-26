
class WordString:

    def __init__(self, string=''):
        self.__string = string

    def __call__(self, indx):
        return self.string.split()[indx]

    def __len__(self):
        return len(self.string.split())

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value