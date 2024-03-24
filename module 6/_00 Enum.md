# Enum

Модуль `enum` содержит в себе тип для перечисления значений с возможностью итерирования и сравнения. 

Его можно использовать для создания понятных обозначений вместо использования чисел (для которых приходится помнить, какое число что обозначает) или строк (в которых легко опечататься и не заметить).


```python
from enum import Enum

class Size(Enum):
    S = "small"
    M = "medium"
    L = "large"
    XL = "extra large"

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


for color in Color:
    print(color.name, color.value)

```

Атрибуты класса Enum конвертируются в экземпляры при парсинге. Каждый экземпляр имеет параметр name, в котором хранится название, а также value, в котором хранится установленное значение.

```python
class ColorFlag(IntFlag):
    BLACK = 0
    RED = 1
    GREEN = 2
    BLUE = 4
    PURPLE = RED | BLUE
    WHITE = RED | GREEN | BLUE

```

Пример 1
```python
class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def __repr__(self):
        return f'{self.name},{self.color.name},{self.size.name}'


apple = Product('Apple', Color.GREEN, Size.SMALL)

print(apple)
```


Пример 2
```python
class Country(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

# получение уникальных значений перечисления

country_code_list = list(map(int, Country))
print(country_code_list)

```