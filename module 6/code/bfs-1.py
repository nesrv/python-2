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
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]


    while queue:
        # print(queue)
        cur_vertex = queue.pop(0)
        node = lengths[-1]
        if node == end:
            print(queue)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)

    return lengths

print(bfs(graph, 0, 4))
