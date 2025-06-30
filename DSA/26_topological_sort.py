"""
Title: Topological Sort in Data Structures

Definition:
Topological sort is an ordering of the nodes in a directed acyclic graph (DAG) such that for every directed edge from node A to node B, A comes before B in the ordering.

Problem Statement:
Suppose you want to find the order to take courses where some courses depend on others. Topological sort helps you find a valid order.

Working:
- Use depth-first search (DFS) to visit all nodes.
- Add each node to the order after visiting all its neighbors.
- Reverse the order at the end.

Steps:
1. Mark all nodes as unvisited.
2. For each unvisited node, do DFS.
3. Add nodes to the order after visiting neighbors.
4. Reverse the order for the result.

Example:
Let's find a topological order for a simple course prerequisite graph.
"""

graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

visited = set()
order = []

def dfs(node):
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        order.append(node)

for node in graph:
    dfs(node)

order.reverse()
print("Topological order:", order)

"""
Explanation:
- We used DFS to visit all nodes.
- Each node is added after its neighbors.
- Topological sort is used in scheduling, course planning, and build systems.
""" 