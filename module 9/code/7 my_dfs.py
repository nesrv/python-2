def dfs(graph, start, finish, visited=None, ):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, finish, visited)
    if start==finish:
        print('Можно дойти до', finish)

    for next in graph[start] - visited:
        dfs(graph, next, finish, visited)
    return visited
# {0, 1, 4, 5, 8, 9, 12}

graph = {
    0: {1},
    1: {0,5},
    2: {6},
    3: {7},
    4: {5, 8},
    5: {1, 4},
    6: {2, 10},
    7: {3},
    8: {4,9,12},
    9: {8, 9},
    10: {6, 9, 11, 14},
    11: {10},
    12: {8},
    13: {}
}

res = dfs(graph, 1, finish=12)

print(res)
