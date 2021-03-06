"""
Sudoku solver script using a backtracking algorithm.
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
    Grids are completed when all cells in them contain non-zero values.
    
    Arguments:
        grid {number matrix} -- The matrix to check for unique values on rows and columns
    
    Returns:
        bool -- True if all numbers are unique on their respective rows and columns, otherwise, False
    """
    return not any(0 in row for row in grid)


def is_unique(digit, cell, grid):
    """
    Checks if a given digit is unique across its row, column and subgrid.
    
    Arguments:
        digit {number} -- The digit to check for
        cell {tuple} -- The (x, y) coordinates of the digit on the grid
        grid {number matrix} -- The matrix to check the digit at

    Returns:
        bool -- True if the digit is unique on its respective row, column and subgrid, otherwise, False
    """
    x, y = cell
    x_axis = [row[x] for row in grid]
    y_axis = grid[y]
    
    col_level = (x // 3) * 3
    row_level = (y // 3) * 3
    subgrid = []

    for index, row in enumerate(grid):
        if row_level <= index < row_level + 3:
            subgrid += row[col_level : col_level + 3]

    return digit not in [*y_axis, *x_axis, *subgrid]


def solve(grid):
    """
    Attempts to solve the grid following Sudoku rules, where on a 9x9 grid:
        - Only numbers from 1 to 9 are valid
        - No duplicates on either rows nor columns
        - No duplicates within the special 3x3 subgrids
    
    Arguments:
        grid {number matrix} -- The matrix to solve
    
    Returns:
        solution -- Returns a list of lists filled with numbers if a solution was found, otherwise, False
    """
    if is_completed(grid):
        return grid
    
    x, y = find_empty_location(grid)

    for digit in range(1, 10):
        if is_unique(digit, (x, y), grid):
            grid[y][x] = digit
            
            if solve(grid):
                return grid
                
            grid[y][x] = 0
    
    return False
