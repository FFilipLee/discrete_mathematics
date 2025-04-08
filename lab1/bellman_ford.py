def bellman_ford(graph, start, end):
    distances = {node: 1000000 for node in graph.nodes()}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes()}
    
    for _ in range(len(graph.nodes()) - 1):
        for u, v in graph.edges():
            weight = graph[u][v]['weight']
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
            weight = graph[v][u]['weight']
            if distances[v] + weight < distances[u]:
                distances[u] = distances[v] + weight
                predecessors[u] = v
    
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()
    
    return path, distances[end]
