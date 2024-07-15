#!/usr/bin/python3
"""N queens solver.

This script finds and prints solutions to the N queens problem for a given N.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])

def queens(n, i=0, a=[], b=[], c=[]):
    """Generate solutions for placing N queens on an NxN chessboard.

    Args:
        n (int): The size of the chessboard.
        i (int): Current row being processed.
        a (list): Columns where queens are placed.
        b (list): Diagonal sums where queens are placed.
        c (list): Diagonal differences where queens are placed.

    Yields:
        list: A valid placement of queens for the current configuration.
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

def solve(n):
    """Print all solutions for the N queens problem.

    Args:
        n (int): The size of the chessboard.
    """
    k = []
    i = 0
    for solution in queens(n):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0

solve(n)
