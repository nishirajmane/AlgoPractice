"""
Title: Quick Sort in Data Structures

Definition:
Quick sort is a fast sorting algorithm that uses the divide and conquer approach. It picks a 'pivot' element and partitions the list so that elements less than the pivot come before it and elements greater come after.

Problem Statement:
Suppose you have a large list of numbers and want to sort them quickly. Quick sort helps you do this efficiently by dividing the list into smaller parts.

Working:
- Choose a pivot element from the list.
- Partition the list into two parts: less than pivot and greater than pivot.
- Recursively sort the two parts.
- Combine the sorted parts and the pivot.

Steps to Use Quick Sort:
1. Pick a pivot element.
2. Partition the list around the pivot.
3. Recursively apply quick sort to the sublists.
4. Combine the results.

Example:
Let's sort the list [5, 2, 9, 1, 5] using quick sort.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

numbers = [5, 2, 9, 1, 5]
sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)

"""
Explanation:
- We picked the first element as the pivot.
- We divided the list into numbers less than and greater than the pivot.
- We sorted each part and combined them.
- Quick sort is very fast for large lists.
""" 