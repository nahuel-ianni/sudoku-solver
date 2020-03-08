"""[summary]
"""

def find_empty_location(grid):
    """
    Looks for the coordinates of the next zero value on the grid,
    starting on the upper left corner, from left to right and top to bottom.

    Keyword Arguments:
        grid {number matrix} -- The matrix to look for the coordinates on (default: {The instance's grid})

    Returns:
        tuple -- The (x, y) coordinates of the next zero value on the grid if one is found
    """
    for index, row in enumerate(grid):
        if 0 in row:
            return (row.index(0), index)


def is_completed(grid):
    """
    Checks if a grid is completed.
    Grids are completed when all cells in a grid contain non-zero values.
    
    Arguments:
        grid {number matrix} -- The matrix to check for unique values on rows and columns
    
    Returns:
        Boolean -- True if all numbers are unique on their respective rows and columns, otherwise, False
    """
    return not any(0 in row for row in grid)


def is_safe(grid, cell, digit):
    """Checks if a given digit is unique across its row, column and subgrid.
    
    Arguments:
        grid {number matrix} -- The matrix to check the digit at
        cell {tuple} -- The (x, y) coordinates of the digit on the grid
        digit {number} -- The digit to check for

    Returns:
        Boolean -- True if the digit is unique on its respective row and column, otherwise, False
    """
    y, x = cell

    if digit in [*grid[x], *[row[y] for row in grid]]:
        return False

    row_level = x // 3
    col_level = y // 3
    subgrid = []
    
    for index, row in enumerate(grid):
        if index in range(row_level * 3, row_level * 3 + 3):
            subgrid.append(row[col_level * 3 : col_level * 3 + 3])

    if digit in subgrid:
        return False

    return True


def solve(grid):
    """
    Attempts to solve the grid following Sudoku rules, where on a 9x9 grid:
        - Only numbers from 1 to 9 are valid
        - No duplicates on either rows nor columns
        - No duplicates within the special 3x3 subgrids
    """
    raise NotImplementedError
