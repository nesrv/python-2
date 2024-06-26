import itertools
from itertools import product

print('Задача 3')
w = 'ГОД'
words = product(w, repeat=6)
counter = 0
for word in words:
    if word[0] == "Г" or word[0] == "Д":
        counter += 1
print(counter) #486

print('Задача 4')
class pairMaker:
    def __init__(self, men=None, women=None):
        self.men = men
        self.women = women
    def couples(self):
        # пары = комбинация двух списков
        all_list = [self.men, self.women]
        rez = list(itertools.product(*all_list))
        return rez
    def counter(self):
        return len(self.couples())
men = ['Иван', 'Сергей']
women = ['Мария', 'Анна', 'Зоя']
pairs = pairMaker(men, women)
print(*pairs.couples())
# ('Иван', 'Мария') ('Иван', 'Анна') ('Иван', 'Зоя') ('Сергей', 'Мария') ('Сергей', 'Анна') ('Сергей', 'Зоя')
print(pairs.counter()) # 6

print('Задача 5')
import itertools
all_list = [[1, 3, 4], [6, 7, 9], [8, 10, 5] ]
rez = list(itertools.product(*all_list))
print(rez)
print(f'Количество {len(rez)}') #Количество 27