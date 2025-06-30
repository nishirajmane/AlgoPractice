"""
Title: Stacks in Data Structures

Definition:
A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means the last element added is the first one to be removed.

Problem Statement:
Suppose you want to keep track of the pages you visit in a web browser so you can go back to the previous page. A stack helps you do this easily.

Working:
- Elements are added (pushed) and removed (popped) from the top of the stack.
- You can only access the top element directly.

Steps to Use a Stack:
1. Create an empty stack.
2. Push elements onto the stack.
3. Pop elements from the stack.
4. Peek at the top element.

Example:
Let's create a stack to store numbers and show push and pop operations.
"""

stack = []  # Creating an empty stack

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushing 10, 20, 30:", stack)

# Pop element
popped = stack.pop()
print("Popped element:", popped)
print("Stack after popping:", stack)

# Peek at the top element
if stack:
    print("Top element:", stack[-1])
else:
    print("Stack is empty.")

"""
Explanation:
- We used a Python list as a stack.
- append() adds (pushes) elements to the top.
- pop() removes (pops) the top element.
- The last element added is the first to be removed (LIFO).
""" 