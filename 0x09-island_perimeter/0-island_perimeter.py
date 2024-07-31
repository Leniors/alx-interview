#!/usr/bin/python3
"""
0-islan_perimeter

A function that returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """island_perimeter
    This method takes a list of integers lists and that represents a grid
    of water and land. Which then calculates the perimeter of the land
    and returns that number

    Arguments:
        grid (2D List): A list of integers where 0 represents water &
                        1 represents land.

    Return:
        (int): The perimeter of the grid passed to the function.
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