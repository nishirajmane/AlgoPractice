"""
Title: Linked Lists in Data Structures

Definition:
A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations.

Problem Statement:
Suppose you want to store a list of names, but you don't know how many names you will have. A linked list allows you to add or remove names easily without worrying about the size.

Working:
- Each node contains data and a reference (link) to the next node.
- The first node is called the head.
- The last node points to None (end of the list).

Steps to Use a Linked List:
1. Create a node class.
2. Link nodes together.
3. Traverse the list to access elements.

Example:
Let's create a simple linked list with 3 names and print them.
"""

# Node class
class Node:
    def __init__(self, data: str):
        self.data: str = data
        self.next: 'Node | None' = None

# Create nodes
node1 = Node("Alice")
node2 = Node("Bob")
node3 = Node("Charlie")

# Link nodes
node1.next = node2
node2.next = node3

# Print the linked list
current = node1
while current:
    print(current.data)
    current = current.next

"""
Explanation:
- We created three nodes with names.
- Each node points to the next node.
- We used a loop to print all names in the linked list.
- Linked lists are useful when you need to add or remove items often.
""" 