#!/usr/bin/python3

"""
Pascal's triangle module.
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
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
