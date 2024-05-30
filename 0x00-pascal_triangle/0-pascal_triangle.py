#!/usr/bin/python3
"""
Pascal triangle
"""

def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows in triangle.

    Returns:
        list: Pascal's triangle as a list of lists.

    Raises:
        ValueError: If n <= 0.

    """
    x = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(x[i - 1][j - 1] + x[i - 1][j])
        row.append(1)
        x.append(row)

    return x
