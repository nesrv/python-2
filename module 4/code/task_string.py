
class StringDigit(str):

    def __init__(self, string):
        if string.isdigit():
            self.string = string
        else:
            raise ValueError("в строке должны быть только цифры")


    def __add__(self, other):
        if isinstance(other, StringDigit):
            other = other.string

        self.string += other
        return StringDigit(self.string)

    def __radd__(self, other):
        if isinstance(other, StringDigit):
            other = other.string
        return StringDigit(other)+self.string

# ------------------------------------------

class StringDigit(str):
    def __init__(self, string):
        if string.isdigit():
            self.string = string
        else:
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return StringDigit(self.string + other)

    def __radd__(self, other):
        return StringDigit(other + self.string)

string = '12455752345950'

sd = StringDigit(string)
sd = sd + "123"
print(sd)
sd = "123" + sd
print(sd)