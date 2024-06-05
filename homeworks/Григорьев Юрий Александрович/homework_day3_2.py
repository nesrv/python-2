class Car:
    def __init__(self, gas=10, capacity=50, gas_per_km=10):
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.gas = gas
        self.odometer = 0

    def fill(self, litrs):
        if self.gas + litrs <= self.capacity:
            self.gas += litrs
        else:
            print(f"Лишние {litrs - (self.capacity - self.gas)} литров не влезли в бак.")
            self.gas = self.capacity

    def ride(self, distance):
        if self.gas >= distance * self.gas_per_km:
            self.odometer += distance
            self.gas -= distance * self.gas_per_km
            print(f"Проехали {distance} километров.")
        else:
            max_distance = self.gas / self.gas_per_km
            print(f"Недостаточно топлива, чтобы проехать {distance} км. Максимально возможное расстояние: {max_distance} км.")


def main():
    car1 = Car(0,20,1)
    n = int(input("Введите количество литров, которые хотите залить в бак: "))
    car1.fill(n)
    k = float(input("Введите как далеко планируете проехать (в км): "))
    car1.ride(k)
    print(f"Бак заполнен на {car1.gas} литров, пробег: {car1.odometer} км.")


if __name__ == "__main__":
    main()