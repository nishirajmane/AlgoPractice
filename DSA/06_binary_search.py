"""
Title: Binary Search in Data Structures

Definition:
Binary search is a fast searching algorithm that works on sorted lists. It repeatedly divides the search interval in half to find the target value.

Problem Statement:
Suppose you have a sorted list of numbers and want to find if a particular number exists. Binary search helps you do this much faster than linear search.

Working:
- Start with the middle element of the list.
- If the target is equal to the middle element, you found it!
- If the target is less, search the left half. If more, search the right half.
- Repeat until you find the target or the list is empty.

Steps to Use Binary Search:
1. Set low and high pointers to the start and end of the list.
2. Find the middle index.
3. Compare the middle element with the target.
4. Adjust the pointers and repeat until found or not found.

Example:
Let's search for the number 25 in a sorted list of numbers.
"""

numbers = [10, 20, 25, 30, 40]
target = 25
low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print(f"Found {target} at index {mid}")
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"{target} not found in the list.")

"""
Explanation:
- We checked the middle number each time.
- If the target was smaller, we searched the left half; if larger, the right half.
- Binary search is much faster than linear search for large, sorted lists.
""" 