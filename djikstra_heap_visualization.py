import heapq
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

def visualize_dijkstra():
    G = nx.Graph()
    edges = [
        (0, 1, {'weight': 7}),
        (0, 2, {'weight': 9}),
        (0, 5, {'weight': 14}),
        (1, 2, {'weight': 10}),
        (1, 3, {'weight': 15}),
        (2, 3, {'weight': 11}),
        (2, 5, {'weight': 2}),
        (3, 4, {'weight': 6}),
        (4, 5, {'weight': 9})
    ]
    G.add_edges_from(edges)
    
    start_node = 0
    
    distances = {node: float('inf') for node in G.nodes()}
    distances[start_node] = 0
    heap = [(0, start_node)]
    visited = set()
    previous = {}
    current_node = None
    
    pos = {
        0: (0, 0.5),
        1: (1, 1),
        2: (1.5, 0.25),
        3: (2, 1),
        4: (3, 0.5),
        5: (2, -1)
    }
    
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.title("Алгоритм Дейкстры с черпаками")
    
    step = 0
    
    def update(frame):
        nonlocal step, heap, visited, current_node
        
        ax.clear()
        
        if frame == 0:
            status = "Инициализация: добавляем стартовую вершину 0 в черпак"
        elif heap:
            current_dist, current_node = heapq.heappop(heap)
            
            if current_node not in visited:
                visited.add(current_node)
                step += 1
                status = f"Шаг {step}: Обрабатываем вершину {current_node}"
                
                for v, data in G[current_node].items():
                    weight = data['weight']
                    if distances[v] > distances[current_node] + weight:
                        distances[v] = distances[current_node] + weight
                        previous[v] = current_node
                        heapq.heappush(heap, (distances[v], v))
            else:
                status = f"Шаг {step}: Пропускаем уже обработанную вершину {current_node}"
        else:
            status = "Алгоритм завершен!"
        
        node_colors = []
        for node in G.nodes():
            if node in visited:
                node_colors.append('green')
            elif node in [x[1] for x in heap]:
                node_colors.append('yellow')
            else:
                node_colors.append('red')
        
        edge_colors = []
        edge_widths = []
        for u, v in G.edges():
            if (u in previous and previous[u] == v) or (v in previous and previous[v] == u):
                edge_colors.append('green')
                edge_widths.append(3)
            else:
                edge_colors.append('black')
                edge_widths.append(1)
        
        nx.draw(G, pos, with_labels=True, node_color=node_colors, 
               edge_color=edge_colors, width=edge_widths, ax=ax)
        
        for node, (x, y) in pos.items():
            ax.text(x, y+0.15, f'd={distances[node]}', 
                    bbox=dict(facecolor='white', alpha=0.7))
        
        for (u, v, data) in G.edges(data=True):
            x = (pos[u][0] + pos[v][0])/2
            y = (pos[u][1] + pos[v][1])/2
            ax.text(x, y, f"{data['weight']}", bbox=dict(facecolor='white', alpha=0.7))
        
        queue_text = "Черпак (очередь):\n" + "\n".join([f"Вершина {v}, d={d}" 
                                                      for d, v in heap])
        ax.text(1.05, 0.9, queue_text, transform=ax.transAxes,
                bbox=dict(facecolor='white', alpha=0.7))
        
        ax.set_title(status)
        plt.tight_layout()
    
    ani = FuncAnimation(fig, update, frames=range(15), interval=1000, repeat=False)
    plt.show()

visualize_dijkstra()
