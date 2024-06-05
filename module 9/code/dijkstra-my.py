nodes = ('1', '2', '3', '4', '5', '6')
distances = {
    '1': {'2': 2, '3': 5},
    '2': {'4': 6, '5': 10},
    '3': {'5': 8, '4': 4},
    '4': {'6': 4},
    '5': {'6': 3},
    '6': {},
}

unvisited = {node: None for node in nodes}
visited = {}
current = '1'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for vertex, distance in distances[current].items():
        if vertex not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[vertex] is None or unvisited[vertex] > newDistance:
            unvisited[vertex] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visited)
