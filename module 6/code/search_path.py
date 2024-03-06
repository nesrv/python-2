graph = {
    1: {2},
    2: {1, 3},
    3: {2, 4},
    4: {3, 5, 8},
    5: {4, 6},
    6: {5, 7},
    7: {6},
    8: {4, 9},
    9: {8, 10},
    10: {9, 11},
    11: {10, 12},
    12: {11}
}

def bfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        # первый путь
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        # перебираем соседние узлы, создаем
        # новый путь и помещаем его в очередь
        for neighbor in graph[node]:
            new_path = path.copy()
            new_path.append(neighbor)
            queue.append(new_path)

print (bfs(graph, 1, 9))