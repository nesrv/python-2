
Мы здесь имеем два абстрактных метода внутри класса `Transport`, причем, первый метод go() - это обычный метод, а второй abstract_class_method() - это абстрактный метод уровня класса. 

Обратите внимание на порядок использования декораторов classmethod и abstractmethod. Они должны быть записаны именно в такой последовательности.


```python
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        """Абстрактный метод класса"""



#Теперь, если объявить какой-либо дочерний класс, например:

class Bus(Transport):
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed

    def go(self):
        print("bus go")

    @classmethod
    def abstract_class_method(cls):
        pass
```

То в нем обязательно нужно переопределить абстрактные методы `go` и `abstract_class_method` класса `Transport`. 

Иначе, объект класса `Bus` не будет создан (возникнет исключение TypeError).

Используя эту информацию, объявите базовый класс Model (модель), в котором нужно объявить один абстрактный метод с сигнатурой:

> def get_pk(self): ...

и один обычный метод:

> def get_info(self): ...

который бы возвращал строку "Базовый класс Model".

На основе класса `Model` объявите дочерний класс `ModelForm`, объекты которого создаются командой:

> form = ModelForm(login, password)

```
где login - заголовок перед полем ввода логина (строка); 
password - заголовок перед полем ввода пароля (строка). 
```

В каждом объекте класса ModelForm должны формироваться локальные атрибуты с именами _login и _password, а также автоматически появляться локальный атрибут _id с уникальным целочисленным значением для каждого объекта класса ModelForm.

В классе ModelForm переопределите метод:

> def get_pk(self): ...

который должен возвращать значение атрибута _id.

Пример использования классов :

```python
form = ModelForm("Логин", "Пароль")
print(form.get_pk())
```

```python
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        print('get_pk')

    @staticmethod
    def get_info(self):
        return f"Базовый класс {__class__.__name__}"


class ModelForm(Model):
    x = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = ModelForm.x # id(self)
        ModelForm.x += 1
    
    def get_pk(self):
        return self._id

  ```