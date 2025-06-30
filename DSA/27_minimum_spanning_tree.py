"""
Title: Minimum Spanning Tree (Kruskal's Algorithm) in Data Structures

Definition:
A minimum spanning tree (MST) is a subset of the edges of a connected, weighted graph that connects all the vertices together with the minimum total edge weight. Kruskal's algorithm is a popular way to find an MST.

Problem Statement:
Suppose you want to connect all cities with the least total cost of roads. MST helps you find the cheapest way to connect everything.

Working:
- Sort all edges by weight.
- Add the smallest edge that doesn't form a cycle.
- Repeat until all nodes are connected.

Steps:
1. Sort all edges by weight.
2. Add the smallest edge that doesn't form a cycle (use disjoint set).
3. Repeat until all nodes are connected.

Example:
Let's find the MST for a simple graph using Kruskal's algorithm.
"""

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parent[yroot] = xroot

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
n = 4
edges.sort(key=lambda x: x[2])
ds = DisjointSet(n)
mst = []
for u, v, w in edges:
    if ds.find(u) != ds.find(v):
        mst.append((u, v, w))
        ds.union(u, v)
print("Edges in MST:", mst)

"""
Explanation:
- We sorted edges and added the smallest ones that didn't form a cycle.
- Disjoint set is used to check for cycles.
- MST is used in network design, road construction, and more.
""" 