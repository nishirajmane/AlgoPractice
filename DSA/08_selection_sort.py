"""
Title: Selection Sort in Data Structures

Definition:
Selection sort is a simple sorting algorithm that repeatedly finds the smallest (or largest) element from the unsorted part and puts it at the beginning.

Problem Statement:
Suppose you have a list of numbers and want to arrange them in ascending order. Selection sort helps you do this by selecting the smallest number each time.

Working:
- Find the smallest element in the unsorted part of the list.
- Swap it with the first element of the unsorted part.
- Move the boundary of the sorted part one step forward.
- Repeat until the list is sorted.

Steps to Use Selection Sort:
1. Start from the first element.
2. Find the smallest element in the rest of the list.
3. Swap it with the current element.
4. Move to the next element and repeat.

Example:
Let's sort the list [5, 2, 9, 1, 5] using selection sort.
"""

numbers = [5, 2, 9, 1, 5]
n = len(numbers)

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print("Sorted list:", numbers)

"""
Explanation:
- We found the smallest number in the unsorted part and swapped it to the front.
- After each pass, the sorted part grows by one.
- Selection sort is easy to understand but not very fast for large lists.
""" 