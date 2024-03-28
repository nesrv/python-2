graph = {
    # список смежности
    0: {1, 3},
    1: {0, 3, 4, 5},
    2: {4, 5},
    3: {0, 1, 5},
    4: {1, 2},
    5: {1, 2, 3},
    6: {7},
    7: {6}
}


def bfs(graph, start, end):
    queue = [[start]]
    # queue.append()
    while queue:
        # формируем путь
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        # перебираем соседние узлы, создаем
        # новый путь и помещаем его в очередь
        for vertex in graph[node]:
            new_path = path.copy()
            new_path.append(vertex)
            queue.append(new_path)



print(bfs(graph, 3, 4))



