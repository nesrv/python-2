## Модуль pickle

Также для работы с бинарными файлами Python предоставляет специальный встроенный модуль `pickle`, который упрощает работу с бинарными файлами. 

Этот модуль предоставляет два метода:

> dump(obj, file): записывает объект obj в бинарный файл file

> load(file): считывает данные из бинарного файла в объект

Допустим, надо надо сохранить значения двух переменных:

```python
import pickle
 
FILENAME = "user.dat"
 
name = "Tom"
age = 19
 
with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
 
with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)

```

Библиотека работает с двоичными потоками данных, как в файл, так и по сети. 

Открыв один поток можно последовательно добавлять в него данные, при этом повторное добавление данных не приводит к их задвоению в итоговом файле, так как модуль `pickle` хранит историю.



```python
class Virus:
    def __init__(self, *args, **kwds):
        print ("я вирус")
    def __call__(self, count):
        for i in range(count):
            print (i, "я размножаюсь")

virus = Virus()


with open('pickle_virus', 'wb') as f:
    pickle.dump(virus, f)


input_file = open('pickle_virus', 'rb') 
func = pickle.load(input_file)
func(10)
```


`Pickle` позволяет сериализовать большое количество разнообразных объектов, используемых в `Python`. 

Можно даже выполнять сериализацию пользовательских классов и функций, с тем нюансом что код функций или классов не сериализуется, а сериализуются только конкретные объекты и ссылки на функции. 