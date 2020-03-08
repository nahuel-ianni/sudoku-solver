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


def is_unique(digit, cell, grid):
    """Checks if a given digit is unique across its row, column and subgrid.
    
    Arguments:
        digit {number} -- The digit to check for
        cell {tuple} -- The (x, y) coordinates of the digit on the grid
        grid {number matrix} -- The matrix to check the digit at

    Returns:
        Boolean -- True if the digit is unique on its respective row, column and subgrid, otherwise, False
    """
    x, y = cell
    column = [row[x] for row in grid]
    row = grid[y]
    
    col_min = (x // 3) * 3
    row_min = (y // 3) * 3
    subgrid = [
        row[col_min : col_min + 3] 
        for index, row in enumerate(grid) 
        if row_min <= index < row_min + 3]

    return digit not in [*row, *column, *subgrid]


def solve(grid):
    """
    Attempts to solve the grid following Sudoku rules, where on a 9x9 grid:
        - Only numbers from 1 to 9 are valid
        - No duplicates on either rows nor columns
        - No duplicates within the special 3x3 subgrids
    """
    raise NotImplementedError
