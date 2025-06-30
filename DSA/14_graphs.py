"""
Title: Graphs in Data Structures

Definition:
A graph is a data structure made up of nodes (also called vertices) and edges that connect pairs of nodes. Graphs can be used to represent networks like roads, social connections, or the internet.

Problem Statement:
Suppose you want to represent a map of cities and the roads connecting them. A graph helps you model this situation.

Working:
- Nodes represent objects (like cities).
- Edges represent connections (like roads).
- Graphs can be directed (one-way) or undirected (two-way).

Steps to Use a Graph:
1. Create a list of nodes (vertices).
2. Create a list of edges (connections between nodes).
3. Traverse the graph (visit nodes in a specific order).

Example:
Let's create a simple graph and print its connections.
"""

# Representing a graph using a dictionary

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Graph connections:")
for node in graph:
    print(f"{node} is connected to {graph[node]}")

"""
Explanation:
- We used a dictionary to represent the graph.
- Each key is a node, and its value is a list of connected nodes.
- Graphs are useful for representing networks and relationships.
""" 