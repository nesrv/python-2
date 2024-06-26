from random import choice


class Coin:
    def __init__(self):
        self.side = None
        self.r = 0
        self.o = 0
        self.plays = 0

    def flip(self):
        self.plays += 1
        if choice(['r', 'o']) == 'o':
            self.side = 'орел'
            self.o += 1
            return f'Выпало: {self.side}'
        else:
            self.side = 'решка'
            self.r += 1
            return f'Выпало: {self.side}'


coin = Coin()

#for i in range(int(input())):
#    coin.flip()

#print(coin.__dict__)



# 2

class Car:
    def __init__(self):
        self.gas = 0
        self.capacity = 60
        self.gas_km = 0.1
        self.odo = 0

    def fill(self, other):
        if self.gas + other > self.capacity:
            print(f'излишки топлива текут по кузову, где-то {other - (self.capacity - self.gas)}л.')
            self.gas = self.capacity
        else:
            self.gas = self.gas + other

    def ride(self, km):
        if km <= self.gas / self.gas_km:
            print(f'проехали {km} километров')
            self.gas -= (self.gas_km * km)
            self.odo += km
        else:
            # print(f'Проехали {int(self.gas / self.gas_km)} километров\nЗаглохли - кончилось топливо\nОсталось {int(km - (self.gas / self.gas_km))}км пути')
            self.odo += self.gas / self.gas_km
            self.gas = 0


car1 = Car()
car1.fill(10)
print(car1.__dict__)
car1.ride(200)
print(car1.__dict__)



