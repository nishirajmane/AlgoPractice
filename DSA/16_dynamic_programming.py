"""
Title: Dynamic Programming in Data Structures

Definition:
Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems and storing the results to avoid repeating work.

Problem Statement:
Suppose you want to find the nth number in the Fibonacci sequence. DP helps you do this efficiently by remembering previous results.

Working:
- Break the problem into smaller subproblems.
- Store the results of subproblems (usually in a list or table).
- Use the stored results to solve bigger problems.

Steps to Use Dynamic Programming:
1. Identify the subproblems.
2. Store the results of subproblems.
3. Build up the solution using the stored results.

Example:
Let's find the 6th Fibonacci number using DP.
"""

def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print("6th Fibonacci number:", fibonacci(6))

"""
Explanation:
- We used a list to store Fibonacci numbers as we calculated them.
- Each number is the sum of the two before it.
- DP saves time by not recalculating the same values.
""" 