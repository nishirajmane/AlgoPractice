 """
Title: Bellman-Ford Algorithm in Data Structures

Definition:
The Bellman-Ford algorithm finds the shortest path from a starting node to all other nodes in a weighted graph, even if some edges have negative weights.

Problem Statement:
Suppose you want to find the shortest route in a city map where some roads have negative tolls (rewards). Bellman-Ford helps you find the shortest paths, even with negative weights.

Working:
- Start from the source node and set its distance to 0, all others to infinity.
- For each edge, update the distance if a shorter path is found.
- Repeat for all edges (V-1) times, where V is the number of vertices.
- Check for negative weight cycles.

Steps:
1. Set the distance to the source as 0, others as infinity.
2. For each edge, update the distance if a shorter path is found.
3. Repeat for all edges (V-1) times.
4. Check for negative weight cycles.

Example:
Let’s find the shortest paths from node 0 in a simple graph.
"""

def bellman_ford(graph, V, E, src):
    dist = [float('inf')] * V
    dist[src] = 0
    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Check for negative-weight cycles
    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return
    print("Vertex \t Distance from Source")
    for i in range(V):
        print(i, "\t", dist[i])

# Example graph: (u, v, w) means edge from u to v with weight w
V = 5
E = 8
graph = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]
bellman_ford(graph, V, E, 0)

"""
Explanation:
- The algorithm finds the shortest path from node 0 to all other nodes, even with negative weights.
- It checks for negative weight cycles.
- Bellman-Ford is used in routing and network protocols.
"""