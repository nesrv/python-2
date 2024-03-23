## Принцип открытости/закрытости

Принцип открытости/закрытости впервые был сформулирован Бернардом Мейером в 1988 году. Роберт К. Мартин говорил о нем так «Наиболее важный принцип открытости/закрытости гласит «Сущности программы (классы, модули, функции и т.п.) должны быть открыты для расширения, но закрыты для изменений».

Следование этому принципу гарантирует, что класс определен достаточно, чтобы делать то, что он должен делать. Добавление любых дополнительных функций может быть реализовано путем создания новых сущностей, которые расширяют возможности существующего класса и добавляют дополнительные функции самим себе. Таким образом можно предотвратить частые и тривиальные изменения в хорошо зарекомендовавшем себя классе низкого уровня. 

Допустим, у нас есть приложение для магазина одежды. Среди функций системы есть функция применения специальных скидок в зависимости от типа одежды. 

Пример ниже показывает один из способов реализации этого требования.

В примере у нас есть класс DiscountCalculator, который умеет хранить тип одежды. В нем есть функция, которая рассчитывает скидку в зависимости от типа одежды и возвращает новую стоимость за вычетом суммы скидки.


```python
from enum import Enum


class Products(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 3


class DiscountCalculator():
    def __init__(self, product_type, price):
        self.product_type = product_type
        self.price = price

    def get_discounted_price(self):
        if self.product_type == Products.SHIRT:
            return self.price - (self.price * 0.10)
        elif self.product_type == Products.TSHIRT:
            return self.price - (self.price * 0.15)
        elif self.product_type == Products.PANT:
            return self.price - (self.price * 0.25)


dc_Shirt = DiscountCalculator(Products.SHIRT, 100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculator(Products.TSHIRT, 100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculator(Products.PANT, 100)
print(dc_Pant.get_discounted_price())

```

Эта конструкция нарушает принцип открытости/закрытости, поскольку этот класс потребует изменения, если будет добавляться какой-то тип одежды или если сумма скидки на какую-либо одежду изменится.

```python
# Open - Close Principle

from abc import abstractmethod, ABC


class DiscountCalculator(ABC):
    @abstractmethod
    def get_discounted_price(self):
        pass


class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, price):
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 0.10)


class DiscountCalculatorTshirt(DiscountCalculator):
    def __init__(self, price):
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 0.15)


class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, price):
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 0.25)


dc_Shirt = DiscountCalculatorShirt(100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculatorTshirt(100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculatorPant(100)
print(dc_Pant.get_discounted_price())

```



Как видно из примера выше, теперь у нас есть очень простой базовый класс DiscountCalculator с одним абстрактным методом get_discounted_price.

Мы создали новые классы для одежды, которые расширяют базовый класс DiscountCalculator. 

Следовательно, теперь каждый подкласс будет реализовывать функционал скидок самостоятельно. 

Сделав так, мы устранили предыдущие ограничения, которые требовали внесения изменений в базовый класс. 

Теперь, не изменяя базовый класс, мы можем добавлять больше одежды, а также изменять размер скидки на отдельный вид одежды по мере необходимости.