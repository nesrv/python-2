# # Модуль 5. Практическая работа

# ## Создание простого интерпретатора арифметических выражений

# ### Основное задание

# import abc
# 
# class InterpreterAbstract(abc.ABC):
#     '''Интерпретатор кода'''
#     
#     def __init__(self, code):
#         '''Принимает код'''
#         self.code = code
#     
#     def execute(self):
#         '''Запускает механизм исполнения кода
#         Возвращает результат исполнения кода'''
#         return self._parse()
#         
#     @abc.abstractmethod
#     def _parse(self):
#         '''Осуществляет парсинг кода.
#         Вызывает _evaluate для исполнения выражений
#         Возвращает результат исполнения кода в excecute''' 
#         pass
#     
#     @abc.abstractmethod
#     def _evaluate(self, code):
#         '''Осуществляет вычисление выражения
#         Возвращает результат выражения в _parse'''      
#         pass


# interpreter = Interpreter('(1+((2+3)*(4*5)))')
# print(interpreter.execute()) # 101
# 
# interpreter = Interpreter('(2+((2*3)/(4^5)))')
# print(interpreter.execute()) # 2
