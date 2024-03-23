## Паттерн Строитель

Рассмотрим пример. 

### Класс пицца

Он принимает заказ, размер, сыр, пеперони (салями) и бекон делать-не делать




```python
class Pizza:
    def __init__(self, size=10, cheese=None, pepperoni=None, bacon=None):
        self.__size = size
        self.__cheese = cheese
        self.__pepperoni = pepperoni
        self.__bacon = bacon

    def __repr__(self):
        recipe = 'Пицца размером ' + str(self.__size) + " с "
        recipe += "сыром " if self.__cheese else ""
        recipe += "пепперони " if self.__pepperoni else ""
        recipe += "беконом" if self.__bacon else ""
        return recipe


pizza = Pizza(12, 1, 1, 1)

print(pizza)
```

По сути – здесь реализован антишаблон. Как не надо делать. Этот антишаблон называется телескопический конструктор. Подзорная труба. Которую использовать не нужно.
Его приходится использовать вот таким образом:

> pizza = Pizza(12, True, False, True)

```python
Сложно понять, что где-что. Не очень удобно.
Было бы удобнее и правильнее сделать так
pizza = PizzaMaker(12)\
   .cheese()\
   .pepperoni()\
   .bacon()\
   .make()

```

Обязательный параметр размер. Всё остальное функционально – через точку. Т.е. может быть или не быть. 

Причем это можно делать в любом порядке.
Как это сделать. Это придумано в шаблоне под названием `builder`


```python
# Паттерн строитель

class PizzaMaker:
    def __init__(self, size=10):
        self.__size = size
        self._cheese = self._pepperoni = self._bacon = False

    def cheese(self):
        self._cheese = True
        return self

    def pepperoni(self):
        self._pepperoni = True
        return self

    def bacon(self):
        self._bacon = True
        return self

    def make(self):
        return self

    def __repr__(self):
        return \
            (f'Пицца {self.__size},'
             f'Бекон: { ("нет", "да")[self._bacon] },'
             f'Сыр: { ("нет", "да")[self._cheese] }, '
             f'Пеперони: { ("нет", "да")[self._pepperoni] }')



pizza = (
    PizzaMaker(12)
    .cheese()
    .bacon()
    .make())


print(pizza)

```

Взяли рецепт. 
Отдаем в производство и в изготовления.
Описываем пицу. Выбираем, что у нас есть. 