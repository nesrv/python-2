## Принцип разделения интерфейсов

Принцип разделения интерфейсов гласит, что «Ни один клиент не должен зависеть от методов, которые он не использует». 


`Принцип разделения интерфейсов` предполагает создание небольших интерфейсов, известных как «ролевые интерфейсы», вместо большого интерфейса, состоящего из нескольких методов. 

Разделяя методы по ролям на более мелкие интерфейсы, клиенты будут зависеть только от методов, которые имеют к ним отношение.

Допустим, мы разрабатываем приложение для различных коммуникационных устройств. 

Мы говорим, что устройство связи – это устройство, которое будет иметь одну или несколько из следующих функций: совершать звонки, отправлять `SMS` или искать в Интернете.

Итак, мы создаем интерфейс с именем `Phone` и добавляем соответствующие абстрактные методы для каждой из этих функций, чтобы любой создаваемый класс смог реализовать эти методы.

Затем мы создаем класс `SmartPhone` с помощью интерфейса `Phone` и реализуем функционал абстрактных методов. 

До сих пор все было в порядке.

Теперь предположим, что нам нужно создать стационарный телефон. 

Он тоже является устройством связи, поэтому мы создаем новый класс `ButtonPhone` через тот же интерфейс `Phone`:
`. 

Именно здесь мы сталкиваемся с проблемой из-за объемного интерфейса `Phone`. 

В классе `ButtonPhone` мы реализовываем метод `make_calls()`, но поскольку мы также наследуем абстрактные методы `send_sms()` и `browse_internet()`, мы должны предоставить реализацию и этих двух абстрактных методов в классе `ButtonPhone`, даже если они в принципе неприменимы к этому виду телефонов.

Мы можем либо создать исключение, либо оставить `pass` вместо реализации, но нам все равно нужно ее предоставить.


```python
from abc import abstractmethod

class Phone:
    @abstractmethod
    def make_calls(self):
        ...
    @abstractmethod
    def send_sms(self):
        ...
    @abstractmethod
    def browse_internet(self):
        ...

class SmartPhone(Phone):
    def make_calls(self):        
        ...
    def send_sms(self):
        ...
    def browse_internet(self):
        ...
class ButtonPhone(Phone):
    def make_calls(self):
        ...
    def send_sms(self):
        ...
    def browse_internet(self):
        ...
```

Все можно исправить, следуя принципу разделения интерфейсов, как в примере ниже.

Вместо создания большого интерфейса мы создаем более маленькие ролевые интерфейсы для каждого метода. 

Соответствующие классы будут использовать только связанные интерфейсы.

```python
from abc import abstractmethod


class CallingDevice:
    @abstractmethod
    def make_calls(self):
        ...


class MessagingDevice:
    @abstractmethod
    def send_sms(self):
        ...


class InternetDevice:
    @abstractmethod
    def browse_internet(self):
        ...


class SmartPhone(CallingDevice, MessagingDevice, InternetDevice):
    def make_calls(self):
        ...

    def send_sms(self):
        ...

    def browse_internet(self):
        ...


class ButtonPhone(CallingDevice, MessagingDevice):
    def make_calls(self):
        ...
class OldPhone(CallingDevice):
    def make_calls(self):

```