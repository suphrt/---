import sys
import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [sys.maxsize] * n
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > distances[u]:
            continue
            
        for v, weight in graph[u]:
            if distances[v] > distances[u] + weight:
                distances[v] = distances[u] + weight
                heapq.heappush(heap, (distances[v], v))
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

