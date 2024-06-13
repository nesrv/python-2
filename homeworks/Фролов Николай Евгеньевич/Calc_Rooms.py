from functools import reduce

rooms = [
   {"name": "кухня", "length": 6, "width": 4},
   {"name": "комната 1", "length": 5.5, "width": 4.5},
   {"name": "комната 2", "length": 5, "width": 4},
   {"name": "комната 3", "length": 7, "width": 6.3},
]

def calculate_area(room):
    return room["length"] * room["width"]

total_area = reduce(lambda x, y: x + y, map(calculate_area, rooms))
print(total_area)
