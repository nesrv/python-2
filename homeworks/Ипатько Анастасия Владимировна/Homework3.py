### Task 1

import random


class Coin:
    def __init__(self):   #n):
         self.side = None
       # self.n = n

    def flip(self, n):
        self.side = random.randint(0, 1)  # random: heads/tails
        self.n = n
        return self.side


n = int(input('Enter qty of coins:'))
count_h = 0
count_t = 0
coin_1 = Coin()

for i in range(n):
    coin = coin_1.flip(n)

    if coin == 0:
        count_t += 1
    else:
        count_h += 1

    print(coin_1.__dict__, count_t, count_h)

print('=' * 40)
print(count_t, count_h)
print((count_t/n)*100, '% Выпадают орлы', (count_h/n)*100, '% Выпадают решки')


### Task2


class Car:
    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km

    def fill(self, qty_l):
        if qty_l < self.capacity:
            print(f'В баке {self.gas + qty_l} литров')
            return self.gas + qty_l

        elif qty_l == self.capacity:
            print(f'В баке {self.gas} литров')
            return self.capacity

        else:
            print(f'Бак полон! Лишние {(self.capacity-qty_l)*(-1)} литров')
            return self.capacity

    def ride(self, qty_km, prob):
        if qty_km * self.gas_per_km == self.gas:
            prob += qty_km
            print(f'Топлива хватит на {qty_km} км. В конце пути бак будет пустым!')
            return qty_km * self.gas_per_km, prob
        elif qty_km * self.gas_per_km < self.gas:
            prob += qty_km
            print(f'Топлива хватит на {qty_km} км. Едем!')
            return qty_km * self.gas_per_km, prob
        else:
            print(f'Топлива хватит только на {((self.gas - qty_km * self.gas_per_km)/self.gas_per_km)*(-1)} км. НЕ едем!')
            return qty_km * self.gas_per_km, prob


car1 = Car(10, 80, 8)
qty_lt = int(input('Введите количество литров: '))
car1 = car1.fill(qty_lt)
print(f'Сейчас в баке {car1} литров!')
qty_k = int(input('Введите количество километров: '))
car_1 = Car(car1, 80, 8)
car_1 = car_1.ride(qty_k, 2000)
print(f'Расход литров топлива на {qty_k} км и пробег машины соответственно: {car_1}')



