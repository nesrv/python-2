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

