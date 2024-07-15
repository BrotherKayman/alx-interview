#!/usr/bin/python3
"""N queens solver.

This script finds and prints solutions to the N queens problem for a given N.
"""

import sys

def is_valid(board, row, col):
    """Check if placing a queen at board[row][col] is valid."""
    n = len(board)
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check upper diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(n):
    """Solve the N queens problem and print all solutions."""
    board = [[0]*n for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([[r, c] for r in range(n) for c in range(n) if board[r][c] == 1])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0
    
    backtrack(0)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
