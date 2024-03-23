from functools import reduce

rooms = [
   {"name": "кухня", "length": 6, "width": 4},
   {"name": "комната 1", "length": 5.5, "width": 4.5},
   {"name": "комната 2", "length": 5, "width": 4},
   {"name": "комната 3", "length": 7, "width": 6.3},
]

print ("Использование только reduce():", reduce(lambda x, y: x + y, (rooms[i]["length"] * rooms[i]["width"] for i in range(len(rooms)))))
print ("Использование reduce() и map():", reduce(lambda x, y: x + y, map(lambda room: room["length"] * room["width"], rooms)))