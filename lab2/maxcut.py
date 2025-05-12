from gurobipy import *
import networkx as nx
import matplotlib.pyplot as plt

n = 14
edges = [
    (0, 1, 4),
    (0, 2, 7),
    (0, 3, 6),
    (0, 4, 5),
    (1, 2, 8),
    (1, 5, 3),
    (2, 6, 2),
    (3, 4, 7),
    (3, 5, 6),
    (4, 6, 4),
    (4, 7, 5),
    (5, 6, 1),
    (5, 8, 6),
    (6, 7, 8),
    (6, 9, 3),
    (7, 8, 2),
    (7, 10, 9),
    (8, 9, 4),
    (8, 11, 7),
    (9, 10, 5),
    (10, 11, 3),
    (10, 13, 2),
    (11, 12, 9),
    (12, 13, 8)
]

model = Model("MaxCut")
x = model.addVars(n, vtype=GRB.BINARY, name="x")
model.setObjective(quicksum(w * (x[i] + x[j] - 2 * x[i] * x[j]) for i, j, w in edges), GRB.MAXIMIZE)
model.setParam("OutputFlag", 0)
model.optimize()

partition = [int(x[i].x) for i in range(n)]
print("Partition:", partition)

G = nx.Graph()
G.add_nodes_from(range(n))
G.add_weighted_edges_from(edges)

node_colors = ['skyblue' if partition[i] == 0 else 'salmon' for i in range(n)]

edge_colors = []
for i, j, w in edges:
    if partition[i] != partition[j]:
        edge_colors.append('red')
    else:
        edge_colors.append('gray')

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)
nx.draw_networkx_labels(G, pos, font_color='black', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): w for i, j, w in edges})
plt.title("Max-Cut Partition Visualization")
plt.axis('off')
plt.show()
