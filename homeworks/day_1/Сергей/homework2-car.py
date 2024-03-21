# Домашка 2. Автомобиль.

class Car:

    def __init__(self, gas=0, tank_capacity=50, gas_per_km=0.1, odo=0):
        self.gas = gas
        self.tank_capacity = tank_capacity
        self.gas_per_km = gas_per_km
        self.odo = odo

    def __repr__(self):
        return f"Автомобиль: кол-во бензина {self.gas} л, объем бака {self.tank_capacity} л, расход {self.gas_per_km} л/км, пробег {self.odo} км"

    def fill(self, new_gas):
        if self.gas + new_gas < self.tank_capacity:
            # Имеющегося и заправляемого бензина меньше, чем емкость бака
            self.gas += new_gas
            print(f"Заправлено {new_gas} л, теперь в баке {self.gas} л")
        elif self.gas + new_gas == self.tank_capacity:
            # Имеющегося и заправляемого бензина ровно столько же, сколько помещается в баке
            self.gas = self.tank_capacity
            print(f"Заправлено {new_gas} л до полного бака")
        elif self.gas == self.tank_capacity:
            # Бак уже полный
            print("Бак полный, заправка не требуется")
        else:
            # Заправляем слишком много, остается лишний бензин
            rest_gas = self.gas + new_gas - self.tank_capacity
            self.gas = self.tank_capacity
            print(f"Заправлено {new_gas - rest_gas} л до полного бака, осталось лишних {rest_gas} л.")

    def ride(self, distance):
        if self.gas >= distance * self.gas_per_km:
            # Бензина хватает на всю поездку
            self.gas -= distance * self.gas_per_km
            self.odo += distance
            print(f"Проехали {distance} км, в баке осталось {self.gas} л, на одометре {self.odo} км")
        elif 0 < self.gas < distance * self.gas_per_km:
            # Бензина не хватает на всю поездку
            actual_distance = self.gas / self.gas_per_km
            self.gas = 0
            self.odo += actual_distance
            print(f"Проехали {actual_distance} км, бензин закончился, на одометре {self.odo} км")
        else:
            # Бензина нет
            print("Бензина нет, ехать не получится")


car1 = Car()

print(car1)

car1.fill(37.5)
car1.fill(12.49)
car1.fill(0.01)
car1.fill(3)
car1.ride(100)
car1.fill(90)
car1.ride(1000)
car1.ride(50)
car1.fill(29.99)
car1.ride(123.45)
