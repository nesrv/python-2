

class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old
    
    def get_info(self):
        return '{}: {}, {}, {}'.format(*self.__dict__.values())

class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight
    

class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
        
        

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):

    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name
