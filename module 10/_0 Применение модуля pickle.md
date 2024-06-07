## Модуль pickle

Также для работы с бинарными файлами Python предоставляет специальный встроенный модуль `pickle`, который упрощает работу с бинарными файлами. 

Этот модуль предоставляет два метода:

> dump(obj, file): записывает объект obj в бинарный файл file

> load(file): считывает данные из бинарного файла в объект

Допустим, надо надо сохранить значения двух переменных:


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