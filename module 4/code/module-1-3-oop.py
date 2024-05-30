# # Модуль 1. Объектно-Ориентированное Программирование
# ## Объектно-Ориентированный Дизайн

# ### SOLID принципы

# ### Single Responsibility Principle

# ### Open/Closed Principle

# import abc

# class АбстрактныйКласс(abc.ABC):
    
    # @abc.abstractmethod
    # def абстрактный_метод(self):
        # pass


# class КонкретныйКласс(АбстрактныйКласс):
    # pass

# объект = КонкретныйКласс() # Ошибка!


# class КонкретныйКласс(АбстрактныйКласс):
    
    # def абстрактный_метод(self):
        # pass

# объект = КонкретныйКласс()


# ### Liskov's Substitution Principle

# class Птица:
    # def лети(self):
      # print("Полетели")



# def полетаем(птица):
    # if isinstance(птица, Птица):
        # птица.лети()
        

# class Сокол(Птица): pass


# сокол = Сокол()
# полетаем(сокол)


# class Страус(Птица): pass

# страус = Страус()
# полетаем(страус)


# ### Опасности:


# class Птица:
    # def лети(self):
        # print("Полетели") 
        # return 'сколько-то километров'
    


# def полетаем(птица):
    # if isinstance(птица, Птица):
        # расстояние = птица.лети() 
        # print(расстояние)
            


# class Сокол(Птица):
    # def лети(self, x): # !!!
        # print("Полетели")
        !!!
        


# ### The Interface Segregation Principle

# import abc

# class ИнтерфейсПтицы(abc.ABC):
    
    # @abc.abstractmethod
    # def ешь(self):
        # pass
    
    # @abc.abstractmethod
    # def иди(self):
        # pass
    
    # @abc.abstractmethod
    # def чирикай(self):
        # pass
    
    # @abc.abstractmethod
    # def лети(self):
         # pass 
        

# import abc

# class ИнтерфейсПтицы(abc.ABC):
    
    # @abc.abstractmethod
    # def ешь(self):
        # pass
    # Другие абстрактные методы
    
# class ИнтерфейсЛетающейПтицы(ИнтерфейсПтицы):
    # @abc.abstractmethod
    # def лети(self):
         # pass
        


# def полетаем(птица):
    # if isinstance(птица, ИнтерфейсЛетающейПтицы):
        # расстояние = птица.лети() 
        # print(расстояние)
            

# class Сокол(ИнтерфейсЛетающейПтицы):
    # def ешь(self):
        # print("Поел") 
    # Реализация остальных методов    
    # def лети(self):
        # print("Полетели")
        
# class Страус(ИнтерфейсПтицы):
    # def ешь(self):
        # print("Поел")
    # Реализация остальных методов
            


# ### Dependency inversion principle

# class FileRead:
    # def __init__(self, name):
        # self._name = name
    # def read(self):
        # print(f'Читаем из файла {self._name}')
        # return 'Прочитали из файла'

# class KeyboardRead:
    # def readln(self):
        # print('Читаем с клавиатуры')
        # return 'Прочитали ввод с клавиатуры'

# class SendMessage:
    # def send(self, msg):
        # print(f'Послали сообщение: {msg}')


# class Processing:
    # def __init__(self, read, send): 
        # if not isinstance(read, FileRead):
            # raise TypeError('Ошибка при чтении из файла')
        # if not isinstance(send, SendMessage):
            # raise TypeError('Ошибка при отправке сообщения')
        # self._reader = read 
        # self._sender = send 
  
    # def process(self):
        # msg = self._reader.read()
        # self._sender.send(msg)


# f = FileRead("file.txt")
# s = SendMessage()
# p = Processing(f, s)
# p.process()



# import abc
# class IReader(abc.ABC):
    # @abc.abstractmethod
    # def read(self):
        # pass

# class IWriter(abc.ABC):
    # @abc.abstractmethod
    # def write(self, msg):
        # pass


# class InputKeyboard(IReader):
    # def read(self):
        # return 'Прочитали ввод с клавиатуры'

# class OutputNetwork(IWriter):
    # def write(self, msg):
        # print(f"Послали сообщение {msg} по сети")

# class Processing:
    # def __init__(self, input, output): 
        # if not isinstance(input, IReader):
            # raise TypeError('Ошибка при чтении данных')
        # if not isinstance(out, IWriter):
            # raise TypeError('Ошибка при записи данных')
        # self._input = input 
        # self._output = output 
  
    # def process(self):
        # msg = self._input.read()
        # self._output.write(msg)
        
# kbd = InputKeyboard()
# net = OutputNetwork()
# proc = Processing(kbd, net)
# proc.process()


# ### Шаблоны проектирования

# class Pizza:
#     def __init__(self, size, cheese, pepperoni, bacon): 
#         self.__size = size
#         self.__cheese = cheese
#         self.__pepperoni = pepperoni
#         self.__bacon = bacon
# 
#     def show(self):
#         recipe = 'Пицца ' + str(self.__size) + " с "
#         recipe += "сыром, " if self.__cheese else ""
#         recipe += "пепперони, " if self.__pepperoni else ""
#         recipe += "беконом" if self.__bacon else ""
#         return recipe

# pizza = Pizza(12, True, False, True)


# pizza = PizzaMaker(12)\
#    .cheese()\
#    .pepperoni()\
#    .bacon()\
#    .make()
# order = Pizza(pizza)

# ### Шаблон проектирования Builder

# class PizzaMaker:
    # def __init__(self, size):
        # self._size = size
        # self._cheese = False
        # self._pepperoni = False
        # self._bacon  = False
    # def cheese(self):
        # self._cheese = True; return self
    # def pepperoni(self):
        # self._pepperoni = True; return self
    # def bacon(self):
        # self._bacon = True; return self
    # def make(self): return self
    

# class Pizza:
    # def __init__(self, maker: PizzaMaker):
        # self.__size = maker._size
        # self.__cheese = maker._cheese
        # self.__pepperoni = maker._pepperoni
        # self.__bacon = maker._bacon
    # def show(self):
        # recipe = 'Пицца ' + str(self.__size) + " с "
        # recipe += "сыром, " if self.__cheese else ""
        # recipe += "пепперони, " if self.__pepperoni else ""
        # recipe += "беконом" if self.__bacon else ""
        # return recipe
    

# pizza = PizzaMaker(12).cheese().bacon().make()
# order = Pizza(pizza)
# print(order.show())


# ### Взаимосвязи классов


# class A()
    # def fn(self): pass
    
# Наследование и реализация

# class B(A): 
    # pass

# b = B(); 
# b.fn()


# Агрегация

# class C:
    # def __init__(self, obj):
        # self.obj = obj
    # def call_fn(self):
        # self.obj.fn()
# a = A()
# c = C(a)
# c.call_fn()


# Композиция

# class D:
    # def __init__(self):
        # self.obj = A()
    # def call_fn(self):
        # self.obj.fn()
# d = D()
# d.call_fn()
