"""
Title: Binary Trees in Data Structures

Definition:
A binary tree is a tree data structure where each node has at most two children, called the left child and the right child.

Problem Statement:
Suppose you want to organize data in a way that makes searching and inserting efficient. A binary tree helps you do this by arranging data in a hierarchical structure.

Working:
- Each node contains data and two links (left and right) to its children.
- The top node is called the root.
- Nodes with no children are called leaves.

Steps to Use a Binary Tree:
1. Create a node class with data, left, and right.
2. Link nodes to form the tree.
3. Traverse the tree (visit nodes in a specific order).

Example:
Let's create a simple binary tree and print its nodes using in-order traversal.
"""

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: 'Node | None' = None
        self.right: 'Node | None' = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# Create nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order traversal:")
inorder(root)

"""
Explanation:
- We created a binary tree with 5 nodes.
- In-order traversal visits left child, root, then right child.
- Binary trees are useful for organizing data efficiently.
""" 