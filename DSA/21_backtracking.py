"""
Title: Backtracking (N-Queens Problem) in Data Structures

Definition:
Backtracking is a method for solving problems by trying out different possibilities and undoing (backtracking) when a solution is not found. It is used for puzzles and constraint satisfaction problems.

Problem Statement:
Suppose you want to place 4 queens on a 4x4 chessboard so that no two queens attack each other. Backtracking helps you find all possible solutions.

Working:
- Place a queen in a row, then move to the next row.
- If a safe position is not found, backtrack to the previous row and try a new position.

Steps:
1. Start with the first row.
2. Try placing a queen in each column.
3. If safe, move to the next row.
4. If not safe or no columns left, backtrack.

Example:
Let's solve the 4-Queens problem using backtracking.
"""

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row=0, board=None, solutions=None):
    if board is None:
        board = [-1] * n
    if solutions is None:
        solutions = []
    if row == n:
        solutions.append(board[:])
        return solutions
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)
            board[row] = -1
    return solutions

solutions = solve_n_queens(4)
print("Number of solutions:", len(solutions))
for sol in solutions:
    print(sol)

"""
Explanation:
- The algorithm tries to place queens row by row.
- If a position is not safe, it backtracks and tries another.
- Backtracking is used in puzzles, games, and constraint problems.
""" 