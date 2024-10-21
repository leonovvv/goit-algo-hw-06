import networkx as nx
from collections import deque

# Створюємо граф (транспортна мережа міста)
G = nx.Graph()
intersections = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
G.add_nodes_from(intersections)
roads = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), 
         ('E', 'F'), ('F', 'G'), ('D', 'F'), ('B', 'E')]
G.add_edges_from(roads)

# Алгоритм DFS (пошук в глибину)
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path.copy())
            if result is not None:
                return result

    return None

# Алгоритм BFS (пошук в ширину)
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

# Використовуємо алгоритми для пошуку шляху між A і G
start_node = 'A'
end_node = 'G'

dfs_path = dfs(G, start_node, end_node)
bfs_path = bfs(G, start_node, end_node)

# Виводимо результати
print(f"Шлях DFS з {start_node} до {end_node}: {dfs_path}")
print(f"Шлях BFS з {start_node} до {end_node}: {bfs_path}")
