def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

dfs(graph, 1, visited)
