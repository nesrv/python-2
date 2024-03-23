from functools import reduce

class Flat:
    def __init__(self):
        self.rooms = []
    
    def add_room(self,name, length, width):
        if isinstance(length, int | float) and isinstance(width, int | float):
            self.rooms.append({
                'name': name,
                'length': length,
                'width': width
            }
            )
        else:
            raise TypeError("Длинна и ширина должны быть указаны чилами")

    def add_rooms(self, rooms):
        rooms = filter(lambda x: True if isinstance(x['length'], int | float) and isinstance(x['width'], int | float) else False, rooms)
        self.rooms += rooms
   
    @property 
    def area(self):  
        area_of_rooms = map(lambda x: x['length'] * x['width'], self.rooms)
        return reduce(lambda a,b: a + b, area_of_rooms)
        

    def __repr__(self) -> str:
        names = tuple(map(lambda x: x['name'], self.rooms))
        return f"Квартира из {len(self.rooms)} комнат. Комнаты: {','.join(names)}. Площадь квартиры {self.area} кв.м."


rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
    {"name": "детская", "length": "7", "width": 6.3},
    {"name": "гостинная 3", "length": "восемь", "width": 6.3},
]

flat = Flat()
flat.add_rooms(rooms)
print(flat.rooms)
print(flat)
flat.add_room(name='столовая', length=5, width=15)
print(flat)
try:
    flat.add_room(name='столовая', length="восемь", width=15)
except TypeError as e:
    print(e)

