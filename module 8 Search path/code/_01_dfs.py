from pprint import pprint

# from sys import setrecursionlimit
# setrecursionlimit(3000)

graph = {
    0: {1},
    1: {0, 5},
    2: {6},
    3: {7},
    4: {5, 8},
    5: {1, 4},
    6: {2, 10},
    7: {3},
    8: {4, 9, 12},
    9: {8, 10},
    10: {6, 9, 11, 14},
    11: {10},
    12: {8},
    13: {},
    14: {15, 10},
    15: {}

}

visited = [False] * len(graph)
start = 10


def dfs(v):
    visited[v] = v
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


dfs(start)
print(visited)

checkpoint = {
    's1': 0,
    's2': 12,
    's3': 3
}
final = 13


# ===============================================

graph = {
    0: {1},
    1: {0, 5},
    2: {6},
    3: {7},
    4: {5, 8},
    5: {1, 4},
    6: {2, 10},
    7: {3},
    8: {4, 9, 12},
    9: {8, 10},
    10: {6, 9, 11, 14},
    11: {10},
    12: {8},
    13: {},
    14: {15, 10},
    15: {}

}


def dfs(v):
    visited[v] = v
    for w in graph[v]:
        if not visited[w]:
            dfs(w)
    return visited


checkpoint = {
    's-1': 0,
    's-2': 12,
    's-3': 3
}
final = 14

for point, value in checkpoint.items():
    visited = [False] * len(graph)
    path = dfs(value)
    if value in path and final in path:
        print(f"Из точки {point} можно дойти до финиша")
    else:
        print(f"Из точки {point} нельзя дойти до финиша")


# ============================
# don't working     
        graph = {
            0: {1},
            1: {0, 5},
            2: {6},
            3: {7},
            4: {5, 8},
            5: {1, 4},
            6: {2, 10},
            7: {3},
            8: {4, 9, 12},
            9: {8, 10},
            10: {6, 9, 11, 14},
            11: {10},
            12: {8},
            13: {},
            14: {15, 10},
            15: {}
        }
doors = {
    4: 5,
    5: 4,
    12: 13,
    13: 12,
    14: 15,
    15: 14
}
keys = set((7, 10))


def dfs(v):
    visited[v] = v
    for w in graph[v]:
        if not visited[w]:
            dfs(w)
    return visited


checkpoint = {
    's-1': 5,
    # 's-2': 13,
    # 's-3': 3,
    # 's-4': 8
}
final = 0

for point, value in checkpoint.items():
    visited = [False] * len(graph)
    path = dfs(value)
    print(path)
    if key := keys & set(path):
        print('есть ключ', key)
    doors_in_path = set(doors.keys()) & set(path)
    print("На пути есть дверь", doors_in_path)
    if value in path and final in path:
        print(f"Из точки {point} можно дойти до финиша")
    else:
        print(f"Из точки {point} нельзя дойти до финиша")
