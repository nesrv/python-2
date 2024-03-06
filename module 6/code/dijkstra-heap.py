import heapq

graph = {
    '1': {'2': 2, '3': 5},
    '2': {'4': 6, '5': 10},
    '3': {'5': 8, '4': 4},
    '4': {'6': 4},
    '5': {'6': 3}
}



def dijkstra(graph, start):
    # Инициализация словаря для хранения расстояний
    # до каждой вершины. Сначала все расстояния бесконечны.
    distances = {vertex: float('infinity') for vertex in graph}

    # Расстояние до начальной вершины равно 0.
    distances[start] = 0

    # Создаём приоритетную очередь для хранения вершин и их расстояний.
    priority_queue = [(0, start)]
    while priority_queue:
        # Извлекаем вершину с наименьшим расстоянием из очереди.
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущее расстояние до вершины уже больше, чем сохранённое расстояние, игнорируем её.
        if current_distance > distances[current_vertex]:
            continue

        # Рассмотрим все соседние вершины текущей вершины.
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден более короткий путь до соседа, обновим расстояние.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


result = dijkstra(graph, '1')
# Выводим результат.
# print("Кратчайшие расстояния до каждой вершины:")
# for vertex, distance in result.items():
#     print(f"До вершины {vertex}: {distance}")