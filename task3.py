import networkx as nx
import heapq

# Створюємо граф з вагами на ребрах (транспортна мережа міста)
G = nx.Graph()
intersections = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
G.add_nodes_from(intersections)

# Додаємо ребра з вагами (наприклад, ваги можуть бути відстанями або часом проїзду)
roads_with_weights = [
    ('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 5), 
    ('C', 'D', 1), ('C', 'E', 7), ('E', 'F', 3), 
    ('F', 'G', 1), ('D', 'F', 2), ('B', 'E', 6)
]
G.add_weighted_edges_from(roads_with_weights)

# Алгоритм Дейкстри для пошуку найкоротшого шляху з вершини start
def dijkstra(graph, start):
    # Черга для вершин, яку використовуємо в алгоритмі (пріоритетна черга)
    priority_queue = []
    # Ініціалізуємо відстані до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    # Відстань до початкової вершини = 0
    distances[start] = 0
    # Додаємо початкову вершину до черги
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша, ніж збережена, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстань для всіх сусідів
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            # Якщо знайшли коротший шлях до сусіда, оновлюємо його відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Знаходимо найкоротші шляхи від кожної вершини
for start_node in intersections:
    shortest_paths = dijkstra(G, start_node)
    print(f"Найкоротші шляхи з {start_node}: {shortest_paths}")
