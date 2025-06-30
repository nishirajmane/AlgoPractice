"""
Title: Recursion in Data Structures

Definition:
Recursion is a method where a function calls itself to solve a problem. It breaks a problem into smaller, similar subproblems.

Problem Statement:
Suppose you want to calculate the factorial of a number (n!). Recursion helps you solve this by breaking it into smaller multiplications.

Working:
- The function calls itself with a smaller input.
- There is a base case to stop the recursion.

Steps to Use Recursion:
1. Define the base case (when to stop).
2. Call the function itself with a smaller input.
3. Combine the results.

Example:
Let's calculate the factorial of 5 using recursion.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

"""
Explanation:
- The function calls itself with n-1 until it reaches 1.
- The base case is when n is 0 or 1.
- Recursion is useful for problems that can be broken into smaller, similar problems.
""" 