"""
Title: Linear Search in Data Structures

Definition:
Linear search is a simple searching algorithm that checks each element in a list one by one until the desired element is found or the list ends.

Problem Statement:
Suppose you have a list of numbers and you want to find if a particular number exists in the list. Linear search helps you do this easily.

Working:
- Start from the first element and compare it with the target value.
- Move to the next element until you find the target or reach the end of the list.

Steps to Use Linear Search:
1. Start from the first element.
2. Compare each element with the target value.
3. If found, return the index.
4. If not found, return -1.

Example:
Let's search for the number 25 in a list of numbers.
"""

numbers = [10, 20, 25, 30, 40]
target = 25
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Found {target} at index {i}")
        found = True
        break

if not found:
    print(f"{target} not found in the list.")

"""
Explanation:
- We checked each number in the list.
- When we found 25, we printed its index.
- If the number is not found, we print a message.
- Linear search is simple but can be slow for large lists.
""" 