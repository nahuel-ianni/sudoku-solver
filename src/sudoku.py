"""
"""
class Sudoku():
    """
    """    
    def __init__(self, grid):
        self.original = grid
        self.solution = grid


    def find_empty_location(self, grid = None):
        """
        Looks for the coordinates of the next zero value on the grid, 
        starting on the upper left corner, from left to right and top to bottom.
            
        Keyword Arguments:
            grid {number matrix} -- The matrix to look for the coordinates on (default: {The instance's grid})
            
        Returns:
            Tuple: Row, Column -- The coordinates of the next zero value on the grid 
            if one is found, otherwise 'None'
        """
        for index, row in enumerate(grid or self.solution):
            if 0 in row:
                return (index, row.index(0))


    def solve(self):
        """
        Attempts to solve the grid following Sudoku rules, where on a 9x9 grid:
            - Only numbers from 1 to 9 are valid
            - No duplicates on either rows nor columns
            - No duplicates within the special 3x3 subgrids
        """
        pass


def is_completed(grid):
    """
    Checks if a grid is completed.
    Grids are completed when all cells in a grid contain non-zero values.
    
    Arguments:
        grid {number matrix} -- The matrix to check for unique values on rows and columns
    
    Returns:
        Boolean -- True if all numbers are unique on their respective rows and columns, otherwise, False
    """
    return all(all(cell != 0 for cell in row) for row in grid)


def is_safe(grid, cell, digit):
    """Checks if a given digit is unique across its row, column and subgrid.
    
    Arguments:
        grid {number matrix} -- The matrix to check the digit at
        cell {Tuple: Row, Column} -- The coordinates of the digit on the grid
        digit {number} -- The digit to check for

    Returns:
        Boolean -- True if the digit is unique on its respective row and column, otherwise, False
    """
    x, y = cell

    if digit in grid[x] + [row[y] for row in grid]:
        return False

    # TODO: Falta revisar si el numero esta en su submatriz

    return True
