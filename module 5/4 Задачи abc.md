## Задача 1 объявите базовый класс с именем `CountryInterface` со следующими абстрактными методами и свойствами:

* `name` - абстрактное свойство `(property)`, название страны `(строка)`;
* `population` - абстрактное свойство `(property)`, численность населения (целое положительное число);
* `square` - абстрактное свойство `(property)`, площадь страны (положительное число);

* `get_info()` - абстрактный метод для получения сводной информации о стране.

На основе класса `CountryInterface` объявите дочерний класс `Country`, объекты которого создаются командой:

```python
country = Country(name, population, square)
```
В самом классе `Country` должны быть переопределены следующие свойства и методы базового класса:

* `name` - свойство (property) для считывания названия страны (строка);
* `population` - свойство (property) для записи и считывания численности населения (целое положительное число);
* `square` - свойство (property) для записи и считывания площади страны (положительное число);

* `get_info()` - метод для получения сводной информации о стране в виде строки:

> "<название>: <площадь>, <численность населения>"

Пример использования классов :

```python
country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000
```



## Задача 2  В программе объявлены два класса и глобальная переменная:
```python
CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title 
        self.__path = path  
        self.__exts = exts  
```

Вам необходимо объявить класс с именем `FileDialogFactory` (фабрика классов), который бы при выполнении команды:

```python
dlg = FileDialogFactory(title, path, exts)
```
возвращал объект класса `WindowsFileDialog`, если `CURRENT_OS` равна строке `windows`, в противном случае - объект класса `LinuxFileDialog`. 

Объект самого класса `FileDialogFactory` создаваться не должен.

Для реализации такой логики, объявите внутри класса `FileDialogFactory` два статических метода:

```python
def create_windows_filedialog(title, path, exts) 
        # для создания объектов класса WindowsFileDialog;
def create_linux_filedialog(title, path, exts) 
        # для создания объектов класса LinuxFileDialog.
```
Эти методы следует вызывать в магическом методе `__new__()` класса `FileDialogFactory`.

Подумайте, как это правильно сделать, чтобы не создавался объект самого класса, а лишь возвращался объект или класса `WindowsFileDialog`, или класса `LinuxFileDialog`.

Пример использования класса:

```python
dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
```