"""
Title: Disjoint Set (Union-Find) in Data Structures

Definition:
A disjoint set (or union-find) is a data structure that keeps track of a set of elements partitioned into non-overlapping subsets. It supports two main operations: find and union.

Problem Statement:
Suppose you want to check if two people are in the same friend group. Disjoint set helps you quickly find and merge groups.

Working:
- Each element points to a parent. The root is the representative of the set.
- Find returns the root of the set.
- Union merges two sets by connecting their roots.

Steps:
1. Initialize each element as its own set.
2. Use find to get the root of a set.
3. Use union to merge two sets.

Example:
Let's use union-find to group friends.
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

ds = DisjointSet(5)
ds.union(0, 2)
ds.union(4, 2)
ds.union(3, 1)
print("Are 4 and 0 in the same group?", ds.find(4) == ds.find(0))
print("Are 1 and 0 in the same group?", ds.find(1) == ds.find(0))

"""
Explanation:
- Each person starts in their own group.
- Union merges groups, find checks if two are in the same group.
- Disjoint sets are used in network connectivity, Kruskal's MST, and more.
""" 