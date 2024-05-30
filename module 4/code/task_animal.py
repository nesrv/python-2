class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old
        self.info = f'{self.name}: {self.old}, '

    def get_info(self):
        return self.info


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight
        self.info += f'{self.color}, {self.weight}'


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
        self.info += f'{self.breed}, {self.size}'
        
## Объявлять в родительском классе методы для работы с дочерними -  плохая практика. 
