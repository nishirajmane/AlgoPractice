"""
Title: Heap (Min-Heap) in Data Structures

Definition:
A heap is a special tree-based data structure that satisfies the heap property. In a min-heap, the parent node is always less than or equal to its children.

Problem Statement:
Suppose you want to always find the smallest number quickly from a collection. A min-heap helps you do this efficiently.

Working:
- The smallest element is always at the root.
- Insertion and removal keep the heap property using swaps.

Steps:
1. Insert a new element at the end.
2. Swap it up to restore the heap property.
3. To remove the smallest, swap root with last, remove last, and swap down.

Example:
Let's use Python's heapq to create a min-heap and perform operations.
"""

import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print("Heap:", heap)
print("Smallest element:", heapq.heappop(heap))
print("Heap after removal:", heap)

"""
Explanation:
- We used heapq to create a min-heap.
- heappush adds elements, heappop removes the smallest.
- Heaps are used in priority queues, scheduling, and algorithms like Heap Sort.
""" 