"""
Title: AVL Trees in Data Structures

Definition:
An AVL tree is a self-balancing binary search tree where the difference in heights between the left and right subtrees is at most 1 for every node.

Problem Statement:
Suppose you want a binary search tree that stays balanced for fast searching, inserting, and deleting. AVL trees help keep the tree balanced automatically.

Working:
- After every insertion or deletion, the tree checks the balance factor (height difference) of each node.
- If the tree becomes unbalanced, it performs rotations to restore balance.

Steps to Use an AVL Tree:
1. Insert or delete nodes like a normal BST.
2. Check the balance factor after each operation.
3. Perform rotations (left, right, left-right, right-left) if needed.

Example:
Let's insert numbers into an AVL tree and see how it balances itself.
"""

# Simple AVL Tree Node and insertion (without full balancing for simplicity)
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)
    # Left Left
    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    # Right Right
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    # Left Right
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    # Right Left
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    return node

def pre_order(node):
    if not node:
        return
    print(node.key, end=' ')
    pre_order(node.left)
    pre_order(node.right)

root = None
for key in [10, 20, 30, 40, 50, 25]:
    root = insert(root, key)

print("Pre-order traversal of AVL tree:")
pre_order(root)

"""
Explanation:
- The AVL tree keeps itself balanced after each insertion.
- Rotations are used to restore balance if needed.
- AVL trees are useful for fast searching, inserting, and deleting.
""" 