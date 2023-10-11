#!/usr/bin/python3
# 12-pascal_triangle.py
"""Pascal's Triangle function"""

def pascal_triangle(n):
    """Gives Pascal's Triangle
    Returns lists of nos that rep the triangle
    """
    if n <= 0:
        return []

    tringl = [[1]]
    while len(tringl) != n:
        tr = tringl[-1]
        x = [1]
        for i in range(len(tr) - 1):
            x.append(tr[i] + tr[i + 1])
        x.append(1)
        tringl.append(x)
    return tringl
