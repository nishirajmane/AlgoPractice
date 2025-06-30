"""
Title: Arrays in Data Structures

Definition:
An array is a collection of items stored at continuous memory locations. The idea is to store multiple items of the same type together. This makes it easy to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).

Problem Statement:
Suppose you want to store the marks of 5 students. Instead of creating 5 separate variables, you can use an array to store all marks together.

Working:
- Arrays store elements in a fixed-size, sequential order.
- Each element can be accessed using its index (starting from 0).

Steps to Use an Array:
1. Declare the array.
2. Initialize the array with values.
3. Access or modify elements using their index.

Example:
Let's create an array to store marks of 5 students and print them.
"""

# Creating an array (using a Python list)
marks = [85, 90, 78, 92, 88]

# Printing all marks
print("Marks of students:")
for i in range(len(marks)):
    print(f"Student {i+1}: {marks[i]}")

"""
Explanation:
- We created a list called 'marks' with 5 values.
- We used a loop to print each student's mark.
- In Python, arrays are usually implemented as lists.
""" 