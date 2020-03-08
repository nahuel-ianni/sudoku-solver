import unittest

from sudoku import find_empty_location, is_completed, is_unique, solve


class SudokuTest(unittest.TestCase):
    
    # Find empty location function tests

    def test_find_empty_location_no_result(self):
        self.assertIsNone(find_empty_location([[1, 2], [3, 4]]))

    def test_find_empty_location_several_locations(self):
        self.assertEqual(find_empty_location([[1, 0], [0, 0]]), (1, 0))

    def test_find_empty_location_unique_location(self):
        self.assertEqual(find_empty_location([[1, 2], [3, 0]]), (1, 1))

    # Is completed function tests

    def test_is_completed_complete(self):
        self.assertTrue(is_completed([[1]]))    

    def test_is_completed_complete_column(self):
        self.assertTrue(is_completed([[1, 2], [3, 4]]))

    def test_is_completed_complete_row(self):
        self.assertTrue(is_completed([[1, 2]]))

    def test_is_completed_incomplete(self):
        self.assertFalse(is_completed([[0]]))    

    def test_is_completed_incomplete_column(self):
        self.assertFalse(is_completed([[1, 2], [3, 0]]))

    def test_is_completed_incomplete_row(self):
        self.assertFalse(is_completed([[1, 0]]))

    # Is unique function tests

    def test_is_unique_not_on_block_1(self):
        self.assertFalse(is_unique(1, (1, 1), self.unfinished_block_sudoku))
    
    def test_is_unique_not_on_block_2(self):
        self.assertFalse(is_unique(1, (4, 1), self.unfinished_block_sudoku))
    
    def test_is_unique_not_on_block_3(self):
        self.assertFalse(is_unique(1, (7, 1), self.unfinished_block_sudoku))
    
    def test_is_unique_not_on_block_4(self):
        self.assertFalse(is_unique(1, (1, 4), self.unfinished_block_sudoku))
    
    def test_is_unique_not_on_block_5(self):
        self.assertFalse(is_unique(1, (4, 4), self.unfinished_block_sudoku))

    def test_is_unique_not_on_block_6(self):
        self.assertFalse(is_unique(1, (7, 4), self.unfinished_block_sudoku))
    
    def test_is_unique_not_on_block_7(self):
        self.assertFalse(is_unique(1, (1, 7), self.unfinished_block_sudoku))
    
    def test_is_unique_not_on_block_8(self):
        self.assertFalse(is_unique(1, (4, 7), self.unfinished_block_sudoku))

    def test_is_unique_not_on_block_9(self):
        self.assertFalse(is_unique(1, (7, 7), self.unfinished_block_sudoku))
        
    def test_is_unique_not_on_column(self):
        self.assertFalse(is_unique(7, (3, 1), [[1, 3, 5, 7, 9], [2, 4, 6, 0, 0]]))
    
    def test_is_unique_not_on_row(self):
        self.assertFalse(is_unique(8, (4, 0), [[2, 4, 6, 8, 0]]))
    
    def test_is_unique_on_block_1(self):
        self.assertTrue(is_unique(2, (1, 1), self.unfinished_block_sudoku))
    
    def test_is_unique_on_block_2(self):
        self.assertTrue(is_unique(3, (4, 1), self.unfinished_block_sudoku))
    
    def test_is_unique_on_block_3(self):
        self.assertTrue(is_unique(6, (7, 1), self.unfinished_block_sudoku))
    
    def test_is_unique_on_block_4(self):
        self.assertTrue(is_unique(7, (1, 4), self.unfinished_block_sudoku))
    
    def test_is_unique_on_block_5(self):
        self.assertTrue(is_unique(6, (4, 4), self.unfinished_block_sudoku))

    def test_is_unique_on_block_6(self):
        self.assertTrue(is_unique(2, (7, 4), self.unfinished_block_sudoku))
    
    def test_is_unique_on_block_7(self):
        self.assertTrue(is_unique(9, (1, 7), self.unfinished_block_sudoku))
    
    def test_is_unique_on_block_8(self):
        self.assertTrue(is_unique(5, (4, 7), self.unfinished_block_sudoku))

    def test_is_unique_on_block_9(self):
        self.assertTrue(is_unique(7, (7, 7), self.unfinished_block_sudoku))

    def test_is_unique_on_column(self):
        self.assertTrue(is_unique(8, (3, 1), [[1, 3, 5, 7, 9], [2, 4, 6, 0, 0]]))
        
    def test_is_unique_on_row(self):
        self.assertTrue(is_unique(9, (4, 0), [[2, 4, 6, 8, 0]]))  

    # Solve function

    def test_solve_finished_grid_returns_correct_grid(self):
        self.assertEqual(solve(self.finished_sudoku.copy()), self.finished_sudoku)

    def test_solve_unfinished_grid_returns_correct_grid(self):
        self.assertEqual(solve(self.unfinished_sudoku.copy()), self.finished_sudoku)
    
    def test_solve_unsolvable_grid_returns_correct_grid(self):
        self.assertEqual(solve(self.unsolvable_sudoku.copy()), False)

    # Utility functions

    finished_sudoku =[
        [3, 1, 6, 5, 7, 8, 4, 9, 2],
        [5, 2, 9, 1, 3, 4, 7, 6, 8],
        [4, 8, 7, 6, 2, 9, 5, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 7, 4, 8, 6, 3, 1, 2, 5],
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6, 9, 2, 3, 5, 1, 8, 7, 4],
        [7, 4, 5, 2, 8, 6, 3, 1, 9]] 

    unfinished_sudoku =[
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    unfinished_block_sudoku =[
        [3, 1, 6, 5, 7, 8, 4, 9, 2],
        [5, 0, 9, 1, 0, 4, 7, 0, 8],    # 2, 3, 6
        [4, 8, 7, 6, 2, 9, 5, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 0, 4, 8, 0, 3, 1, 0, 5],    # 7, 6, 2
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6, 0, 2, 3, 0, 1, 8, 0, 4],    # 9, 5, 7
        [7, 4, 5, 2, 8, 6, 3, 1, 9]] 

    unsolvable_sudoku = [
        [5, 0, 6, 5, 0, 8, 4, 0, 3],
        [5, 2, 0, 0, 0, 0, 0, 0, 2],
        [1, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


if __name__ == "__main__":
    unittest.main()
