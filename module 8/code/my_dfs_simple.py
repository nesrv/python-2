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
    13: {14},
    14: {13}
}

visited = set()
def dfs(start, end):
    # if v in visited:
    #     print('111')# Если вершина уже посещена, выходим
    #     return
    visited.add(start)  # Посетили вершину v
    if start==end:
        print(end, 'можно')
    # print(v, graph[v])
    for i in graph[start]:  # Все смежные с v вершины
        if not i in visited:
            dfs(i, end)
        else:
            print(visited)


dfs(12, 7)
# print(visited)

# if v in visited:
#     return
