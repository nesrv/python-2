class ListInteger(list):

    def __init__(self, value):
        for v in value:
            if not isinstance(v, int):
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(value)

    def __setitem__(self, key, value):
        if isinstance(value, int):
            super().__setitem__(key, value)
        else:
            raise TypeError('можно передавать только целочисленные значения')

    def append(self, value) -> None:
        if isinstance(value, int):
            super().append(value)
        else:
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError