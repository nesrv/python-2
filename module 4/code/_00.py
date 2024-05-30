# Реализовать класс, наследуемый от класса list и переопределить метод append,
# реализовав в нем не добавление элементов, как по умолчанию, а удаление последнего элемента.
# Разрешить сложение списка со строкой и наоборот
class list(list):
    
    def __str__(self):
        return ",".join(map(str, self))
    
    def append(self):
        self.pop()
    def append_first(self, value):
        self.insert(0, value)

    def __add__(self, other):
        self += [other]
        return self

    def __radd__(self, other):
        v = list(other)
        return v + self




a = list((1,2,3,4))
a.append()
print(a)
a.append_first(100)
a = a + "python"
a = 'c++' + a
print(a)


