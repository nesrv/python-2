# x = 3.5
# print(x.as_integer_ratio())

# y = 15

# print(y.bit_count())
# print(type(y))

# x = bin(y)
# print(x)

from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int
    length: float = field(init=False)
 

    def __post_init__(self):   
        self.length = (self.x ** 2 + self.y ** 2) ** 0.5
    
    
p1 = Point(1,2)
print(p1)
print(p1.__dict__)
print(p1.length)