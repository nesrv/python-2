
## Практические задачи


### Задача 1.

Определите: Из каких точек можно дойти до финиша(F), а из каких нет.

![](img/task1.png)



Выведите ответ в формате:

* Из точки S-1 можно дойти до финиша 
* Из точки S-3 нельзя дойти до финиша

```python
graph = {    

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

visited = [False] * len(graph)
# Реализация 
...
if ...
  print(f"Из точки {point} можно дойти до финиша")
else:
  print(f"Из точки {point} нельзя дойти до финиша")
...

```


