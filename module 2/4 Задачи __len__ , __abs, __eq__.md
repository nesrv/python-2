### Задача 1. 

Объявите класс `WordString`, объекты которого создаются командами:

```python
w1 = WordString()
w2 = WordString(string)
```
где `string` - передаваемая строка. Например:

```python
words = WordString("Курс по Python ООП")
```

Реализовать следующий функционал для объектов этого класса:

`len(words)` - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
`words(indx)` - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).

Также в классе `WordString` реализовать объект-свойство (`property`):

`string` - для передачи и считывания строки.

Пример пользования классом WordString :

```python
words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
```

Заготовка для программы

```python
class WordString:

    def __init__(self, string=''):
        ...

    def __call__(self, indx):
        ...

    def __len__(self):
        ...

    @property
    def string(self):
        ...

    @string.setter
    def string(self, value):
        ...
```



## 2. Найдите точку наиболее удаленную от начала координат и выведите ее координаты. 

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
```

### 3. Как вывести все точки в такой виде ?

```
[Точка (2,7), Точка (12,7), Точка (5,-2), Точка (10,-16), Точка (-12,0)]
```
одной командой `print(points)`


### 4. Как сравнить 2 точки ?

```python
p1 = Point(2, 7)
p2 = Point(2, 7)

print(p1 == p2)
```

### 5. Как отсортировать список точек `points`?
* по координате х
* по удаленности от начала координат


### 6. Как работает len?

```python
print(len(p1))
```
### 7. Как работает abs?

```python

p3 = Point(-2, 7)
abs(p3)
print(p3) # Точка (2,-7)
```

