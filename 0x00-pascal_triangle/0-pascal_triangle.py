#!/usr/bin/python3

def pascal_triangle (n):
    """Returns a list of lists representing Pascal's Triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for i in range(1, n):
        row = [1]  # Each row starts with a '1'
        for j in range(1, i):
            # Each value is the sum of the two values above it in the triangle
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Each row ends with a '1'
        triangle.append(row)

    return triangle
