
class Car:
    def __init__(self, capacity, gas_per_km):
        self.gas = 0
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0

    def fill(self, liters):
        if liters > self.capacity - self.gas:
            print(f"Лишние {liters - (self.capacity - self.gas)} литров")
            self.gas = self.capacity
        else:
            self.gas += liters

    def ride(self, km):
        max_km = self.gas / self.gas_per_km
        if km > max_km:
            print(f"Проехали {max_km} километров")
            self.gas = 0
            self.mileage += max_km
        else:
            print(f"Проехали {km} километров")
            self.gas -= km * self.gas_per_km
            self.mileage += km

car1 = Car(50,  0.12)
car1.fill(80)
car1.ride(900)

