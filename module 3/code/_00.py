# Реализовать класс, наследуемый от класса list и переопределить метод append,
# реализовав в нем не добавление элементов, как по умолчанию, а удаление последнего элемента.

# Разрешить сложение списка со строкой и наоборот
class Vector(list):
    def __str__(self):
        return ",".join(map(str, self))

    def append(self):
        self.pop()

    def __add__(self, other):
        self += other
        return self

    def __radd__(self, other):
        v = Vector(other)
        return v + self


v = Vector([1, 2, 3])
# print(v)

v.append()
# print(v)

v1 = v + 'python'
print(v1)  # 1,2,p,y,t,h,o,n
v2 = 'python' + v  # p,y,t,h,o,n,1,2
print(v2)
