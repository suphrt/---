import sys

def dijkstra(graph, start):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    distances[start] = 0                    
    visited = [False] * num_vertices         
    
    for _ in range(num_vertices):
        min_dist = sys.maxsize
        u = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                u = v
        if u == -1:
            break
        visited[u] = True

        for (v, weight) in graph[u]:
            if distances[v] > distances[u] + weight:
                distances[v] = distances[u] + weight
    
    return distances

graph = [
    [(1, 7), (2, 9), (5, 14)], 
    [(0, 7), (2, 10), (3, 15)],
    [(0, 9), (1, 10), (3, 11), (5, 2)],  
    [(1, 15), (2, 11), (4, 6)],
    [(3, 6), (5, 9)],            
    [(0, 14), (2, 2), (4, 9)]    
]


a = dijkstra(graph, 0)
for i in range(1, len(a)):
    print(f"Кратчайший путь из 0 в {i} =", a[i])
