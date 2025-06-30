"""
Title: Dijkstra's Algorithm in Data Structures

Definition:
Dijkstra's algorithm is used to find the shortest path from a starting node to all other nodes in a weighted graph with non-negative weights.

Problem Statement:
Suppose you want to find the shortest route from your home to all other places in a city map. Dijkstra's algorithm helps you find the shortest paths efficiently.

Working:
- Start from the source node and set its distance to 0, all others to infinity.
- Visit the nearest unvisited node, update the distances to its neighbors.
- Mark the node as visited and repeat until all nodes are visited.

Steps:
1. Set the distance to the source as 0, others as infinity.
2. Pick the unvisited node with the smallest distance.
3. Update the distances to its neighbors.
4. Mark the node as visited.
5. Repeat until all nodes are visited.

Example:
Let's find the shortest paths from node 0 in a simple graph.
"""

import sys

graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

V = len(graph)
def dijkstra(src):
    dist = [sys.maxsize] * V
    dist[src] = 0
    sptSet = [False] * V
    for _ in range(V):
        min_dist = sys.maxsize
        for v in range(V):
            if not sptSet[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        sptSet[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    print("Vertex \t Distance from Source")
    for i in range(V):
        print(i, "\t", dist[i])

dijkstra(0)

"""
Explanation:
- The algorithm finds the shortest path from node 0 to all other nodes.
- It updates distances and marks nodes as visited.
- Dijkstra's is used in maps, GPS, and network routing.
""" 