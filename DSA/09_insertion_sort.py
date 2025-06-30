"""
Title: Insertion Sort in Data Structures

Definition:
Insertion sort is a simple sorting algorithm that builds the final sorted list one item at a time by inserting each new item into its correct position.

Problem Statement:
Suppose you have a list of numbers and want to arrange them in ascending order. Insertion sort helps you do this by inserting each number into its correct place.

Working:
- Start with the second element and compare it with the elements before it.
- Move larger elements one position ahead to make space for the new element.
- Insert the new element in its correct position.
- Repeat for all elements.

Steps to Use Insertion Sort:
1. Start from the second element.
2. Compare it with the elements before it.
3. Move larger elements ahead.
4. Insert the current element in the right place.
5. Repeat for all elements.

Example:
Let's sort the list [5, 2, 9, 1, 5] using insertion sort.
"""

numbers = [5, 2, 9, 1, 5]
n = len(numbers)

for i in range(1, n):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key

print("Sorted list:", numbers)

"""
Explanation:
- We picked each number and inserted it into its correct place.
- Larger numbers were moved ahead to make space.
- Insertion sort is easy to understand and works well for small lists.
""" 