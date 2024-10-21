import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()

# Додаємо вершини (перехрестя)
intersections = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
G.add_nodes_from(intersections)

# Додаємо ребра (дороги між перехрестями)
roads = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), 
         ('E', 'F'), ('F', 'G'), ('D', 'F'), ('B', 'E')]
G.add_edges_from(roads)

# Аналіз основних характеристик
print("Кількість вершин (перехресть):", G.number_of_nodes())
print("Кількість ребер (доріг):", G.number_of_edges())

# Ступінь вершин (кількість доріг з кожного перехрестя)
degrees = {node: G.degree(node) for node in G.nodes()}
print("Ступінь вершин (кількість доріг на перехрестях):", degrees)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u}-{v}" for u, v in G.edges()})
plt.title("Транспортна мережа міста")
plt.show()
