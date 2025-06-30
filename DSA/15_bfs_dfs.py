"""
Title: BFS and DFS in Graphs

Definition:
BFS (Breadth-First Search) and DFS (Depth-First Search) are two ways to traverse (visit all nodes) in a graph or tree.

Problem Statement:
Suppose you want to visit all cities in a map (graph) or find a path between two cities. BFS and DFS help you explore the graph.

Working:
- BFS visits nodes level by level, using a queue.
- DFS visits nodes as far as possible along each branch before backtracking, using a stack or recursion.

Steps for BFS:
1. Start from a node and add it to a queue.
2. Visit the node and add its neighbors to the queue.
3. Repeat until the queue is empty.

Steps for DFS:
1. Start from a node and visit it.
2. Recursively visit each unvisited neighbor.
3. Backtrack when no more neighbors.

Example:
Let's traverse a simple graph using BFS and DFS.
"""

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

def dfs(node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

print("BFS traversal:")
bfs('A')
print("\nDFS traversal:")
dfs('A')

"""
Explanation:
- BFS uses a queue to visit nodes level by level.
- DFS uses recursion to visit nodes deeply before backtracking.
- Both are useful for exploring graphs and finding paths.
""" 