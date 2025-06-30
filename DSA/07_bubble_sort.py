"""
Title: Bubble Sort in Data Structures

Definition:
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

Problem Statement:
Suppose you have a list of numbers and want to arrange them in ascending order. Bubble sort helps you do this by comparing and swapping elements.

Working:
- Compare each pair of adjacent elements.
- Swap them if they are in the wrong order.
- Repeat the process for all elements until the list is sorted.

Steps to Use Bubble Sort:
1. Start from the first element.
2. Compare it with the next element.
3. Swap if needed.
4. Move to the next pair and repeat.
5. Repeat the whole process for all elements.

Example:
Let's sort the list [5, 2, 9, 1, 5] using bubble sort.
"""

numbers = [5, 2, 9, 1, 5]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)

"""
Explanation:
- We compared and swapped adjacent numbers if needed.
- After each pass, the largest number moves to the end.
- Bubble sort is easy to understand but not very fast for large lists.
""" 