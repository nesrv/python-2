# # Модуль 1. Объектно-Ориентированное Программирование
# ## Фундаментальные основы

# ### Программа: чтение с клавиатуры; вывод в терминал.

# def process():
#     msg = input('Введите что-нибудь: ')
#     print(msg)
# 
# process()

# ### Добавляем: чтение из файла

# def file_read():
#     return "Зачитали файл"
# 
# 
# def process(from_file=False):
#     if from_file:
#         msg = file_read()
#     else:  
#         msg = input('Введите что-нибудь: ')
#     print(msg)
# 
# process()
# process(True)

# ### Добавляем: отправить данные по сети

# def file_read():
#     return "Зачитали файл"
# 
# def from_terminal():
#     return input('Введите что-нибудь: ')
# 
# def to_terminal(msg):
#     print(f'Послали в терминал: {msg}')  
# 
# def send_message(msg):
#     print(f"Послали по сети: {msg}")
# 
# def process(from_file=False, send_to=False):
#     if from_file:
#         msg = file_read()
#     else:  
#         msg = from_terminal()
#         if send_to:
#             send_message(msg)
#         else:
#             to_terminal(msg)
# 
# process()
# process(True)
# process(True, True)
# process(False, True)



# ### Классы и объекты

# class ИмяКласса:
    # pass

# Какого класса наш класс?
# type(ИмяКласса)


# Объект - экземпляр данного класса
# объект = ИмяКласса()

# Какого класса наш объект?
# type(объект)




# Является ли наш объект экземпляром конкретного класса?
# isinstance(объект, ИмяКласса)


# ### Методы экземпляра класса

# def имя_метода(self):
#         pass

# # вызов метода
# объект.имя_метода()

# ### Атрибуты экземпляра класса

# def имя_метода(self, параметр):
#         self.имя_атрибута = параметр
#         return self.имя_атрибута

# # вызов метода
# объект.имя_метода('параметр')

# ### Конструктор экземпляра класса

# def __init__(self):
#         # объявление атрибутов
#         self.имя_атрибута = значение

# ### Параметры для конструктора

# def __init__(self, параметр1, параметр2=значение):
#         # объявление атрибутов
#         self.имя_атрибута1 = параметр1
#         self.имя_атрибута2 = параметр2
#         self.имя_атрибута3 = значение

# ### Магия приведения объекта к строке

# def __repr__(self):
#         return 'Привожу к строке когда угодно'
# 
# >>> print(объект)
# >>> объект
# >>> str(объект)

# def __str__(self):
#         return 'Переопределяю __repr__ в некоторых случаях'
# 
# >>> print(объект)
# >>> объект
# >>> str(объект)

# ### ООПринцип № 1: инкапсуляция

# ### Свойства экземпляра класса

# def __init__(self):
#         # нет доступа по соглашению
#         self._protected = значение
#         # конкретно нет доступа
#         self.__private = значение
# 
# def get_private(self):
#         return self.__private
#     
# def set_private(self, value):
#         self.__private = value
#         
# private = property(get_private, set_private)

# объект.private = 100
# 
# print(объект.private)

# ### Декораторы для свойств

# def __init__(self):
#         self.__private = значение
# 
# # getter
# @property 
# def private(self):
#         return self.__private
# # setter    
# @private.setter
# def private(self):
#         self.__private = value

# ### Атрибуты класса

# class ИмяКласса:
    
    # атрибут_класса = значение_по_умолчанию
    
    # def метод(self, параметр):
        # ИмяКласса.атрибут_класса = параметр
        


# объект.метод(значение)

# print(ИмяКласса.атрибут_класса)


# ### Методы класса

# @staticmethod
# def static_method():
#     return ИмяКласса.атрибут_класса

# @classmethod
# def class_method(cls):
#     return cls.атрибут_класса

# #### cls - ссылка на сам класс

# объект.static_method()
# 
# объект.class_method()
