from pprint import pprint

graph = [
    # список смежности в виде списка
    [1, 3],  # 0
    [0, 3, 4, 5],  # 1
    [4, 5],  # 2
    [0, 1, 5],  # 3
    [1, 2],  # 4
    [1, 2, 3],  # 5
    [7],  # 6
    [6]  # 7
]

visited = [False] * (len(graph))
start = 0
res = []
visited1 = [[i, False] for i in range(len(graph))]


def dfs(v):
    visited[v] = True
    visited1[v][1] = True
    for w in graph[v]:
        res.append([v, w])
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


dfs(start)

print(visited)
print('=' * 40)
pprint(visited1, width=20)
print('=' * 40)
pprint(res, width=20)


# ===================================================
# список смежности в виде словаря

graph = {
    0: [1, 3],
    1: [0, 3, 4, 5],
    2: [4, 5],
    3: [0, 1, 5],
    4: [1, 2],
    5: [1, 2, 3],
    6: [7],
    7: [6]
}

visited = [False] * (len(graph))
start = 0


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


dfs(start)

print(visited)


# пример с лабиринтом

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
    12: {11},
}

visited = [False] * (len(graph)+1)
start = 1


def dfs(v):
    visited[v] = v
    print(v)
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


dfs(start)

print(visited)
