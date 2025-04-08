import networkx as nx
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from dijkstra import *
from bellman_ford import *

def generate_grid_graph(N, max_weight):
    G = nx.Graph()
    
    # nodes
    for i in range(N):
        for j in range(N):
            G.add_node((i, j))
    
    # horizontal edges
    for i in range(N):
        for j in range(N-1):
            weight = random.randint(1, max_weight)
            G.add_edge((i, j), (i, j+1), weight=weight)
    
    # vertical edges
    for i in range(N-1):
        for j in range(N):
            weight = random.randint(1, max_weight)
            G.add_edge((i, j), (i+1, j), weight=weight)
    
    return G

def draw_graph(G):
    pos = {(i, j): (j, -i) for i, j in G.nodes()}
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

def visualize_shortest_path(G, path=None):
    pos = {(i, j): (j, -i) for i, j in G.nodes()}
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.show()

grid_graph_3 = generate_grid_graph(3, 20)
grid_graph_10 = generate_grid_graph(10, 20)
grid_graph_17 = generate_grid_graph(17, 20)
grid_graph_32 = generate_grid_graph(32, 20)

draw_graph(grid_graph_10)

graphs = [grid_graph_3, grid_graph_10, grid_graph_17, grid_graph_32]

for graph in graphs:
    nodes = list(graph.nodes())

    dijkstra_times = []
    bellman_ford_times = []

    for i in range(10):
        start, end = random.sample(nodes, 2)
        
        start_time = time.time()
        shortest_path_dijkstra, total_distance_dijkstra = dijkstra(graph, start, end)
        dijkstra_time = (time.time() - start_time) * 1000
        dijkstra_times.append(dijkstra_time)

        start_time = time.time()
        shortest_path_bellman, total_distance_bellman = bellman_ford(graph, start, end)
        bellman_time = (time.time() - start_time) * 1000
        bellman_ford_times.append(bellman_time)

        # print(f"Start node: {start}")
        # print(f"End node: {end}")
        # print(f"Shortest path dijkstra: {shortest_path_dijkstra}")
        # print(f"Total distance dijkstra: {total_distance_dijkstra}")
        # print(f"Shortest path bellman: {shortest_path_bellman}")
        # print(f"Total distance bellman: {total_distance_bellman}")

    print(f"\nStatistics for graph with {len(nodes)} nodes and {len(graph.edges())} edges:")
    
    print("\nDijkstra's Algorithm:")
    print(f"Min time: {np.min(dijkstra_times):.4f} ms")
    print(f"Max time: {np.max(dijkstra_times):.4f} ms")
    print(f"Avg time: {np.mean(dijkstra_times):.4f} ms")
    print(f"Std dev: {np.std(dijkstra_times):.4f} ms")
    
    print("\nBellman-Ford Algorithm:")
    print(f"Min time: {np.min(bellman_ford_times):.4f} ms")
    print(f"Max time: {np.max(bellman_ford_times):.4f} ms")
    print(f"Avg time: {np.mean(bellman_ford_times):.4f} ms")
    print(f"Std dev: {np.std(bellman_ford_times):.4f} ms")
    print("\n" + "="*50 + "\n")
