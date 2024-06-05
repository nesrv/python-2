from functools import reduce

# Функция для вычисления площади комнаты
def calculate_area(room):
    return room["length"] * room["width"]

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

# Вычисляем площади всех комнат
areas = map(calculate_area, rooms)

# Суммируем площади всех комнат
total_area = reduce(lambda x, y: x + y, areas)

print("Площадь каждой комнаты:")
for room in rooms:
    print(f"{room['name']}: {calculate_area(room)} кв.м")

print(f"\nОбщая площадь квартиры: {total_area} кв.м")