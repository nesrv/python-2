from abc import ABC, abstractmethod, abstractproperty

from abc import ABC, abstractmethod

class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        return

    @property
    @abstractmethod
    def population(self):
        return

    @property
    @abstractmethod
    def square(self):
        return

    @abstractmethod
    def get_info(self):
        return


class Country(CountryInterface):

    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square
        
    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"
# -----------------------------------------------------

class CountryInterface(ABC):

    @abstractproperty
    def name(self):
        '''Не определено объект-свойство для записи и считывания название страны'''

    @abstractproperty
    def population(self):
        '''Не определено объект-свойство для записи и считывания численности населения'''

    @abstractproperty
    def square(self):
        '''Не определено объект-свойство для записи и считывания площади страны'''

    @abstractmethod
    def get_info(self):
        '''Не определен метод get_info для получения сводной информации о стране.'''


class Country(CountryInterface):
    def __init__(self, name, population, square) -> None:
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"
    
country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0

print(country.get_info()) # Россия: 354005483.0, 150000000


# -------------------------------------------------