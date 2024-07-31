#!/usr/bin/python3
"""
0-island_perimeter.py
"""

def island_perimeter(grid):
    """
    inspect the grid and get its perimeter
    """
    
    perimeter = 0
    
    for i in range(len(grid) - 1):
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == 1:
                add = 4
            else:
                continue

            if grid[i][j] == 1 and j > 0 and grid[i][j - 1] == 1:
                add -= 2

            if grid[i][j] == 1 and i > 0 and grid[i - 1][j] == 1:
                add -= 2

            perimeter += add

    return perimeter