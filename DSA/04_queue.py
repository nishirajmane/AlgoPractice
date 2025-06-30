"""
Title: Queues in Data Structures

Definition:
A queue is a linear data structure that follows the First In First Out (FIFO) principle. This means the first element added is the first one to be removed.

Problem Statement:
Suppose you are waiting in line to buy movie tickets. The person who comes first gets the ticket first. A queue helps you manage such situations.

Working:
- Elements are added (enqueued) at the rear (end) and removed (dequeued) from the front (beginning).
- You can only access the front and rear elements directly.

Steps to Use a Queue:
1. Create an empty queue.
2. Enqueue (add) elements to the rear.
3. Dequeue (remove) elements from the front.
4. Peek at the front element.

Example:
Let's create a queue to store numbers and show enqueue and dequeue operations.
"""

from collections import deque

queue = deque()  # Creating an empty queue

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueuing 10, 20, 30:", list(queue))

# Dequeue element
removed = queue.popleft()
print("Dequeued element:", removed)
print("Queue after dequeuing:", list(queue))

# Peek at the front element
if queue:
    print("Front element:", queue[0])
else:
    print("Queue is empty.")

"""
Explanation:
- We used Python's deque as a queue.
- append() adds (enqueues) elements to the rear.
- popleft() removes (dequeues) the front element.
- The first element added is the first to be removed (FIFO).
""" 