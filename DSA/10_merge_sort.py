"""
Title: Merge Sort in Data Structures

Definition:
Merge sort is a sorting algorithm that divides the list into halves, sorts each half, and then merges them back together. It uses the divide and conquer approach.

Problem Statement:
Suppose you have a large list of numbers and want to sort them efficiently. Merge sort helps you do this by breaking the problem into smaller parts.

Working:
- Divide the list into two halves.
- Recursively sort each half.
- Merge the sorted halves back together.

Steps to Use Merge Sort:
1. Divide the list into two halves.
2. Sort each half using merge sort.
3. Merge the two sorted halves.
4. Repeat until the whole list is sorted.

Example:
Let's sort the list [5, 2, 9, 1, 5] using merge sort.
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

numbers = [5, 2, 9, 1, 5]
merge_sort(numbers)
print("Sorted list:", numbers)

"""
Explanation:
- We divided the list into halves and sorted each half.
- Then we merged the sorted halves together.
- Merge sort is efficient for large lists and uses the divide and conquer method.
""" 