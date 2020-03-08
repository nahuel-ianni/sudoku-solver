import unittest

from sudoku import find_empty_location, is_completed, is_safe, solve


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

    # Is safe function tests

    def test_is_safe_not_on_column(self):
        self.assertFalse(is_safe([[1, 3, 5, 7, 9], [2, 4, 6, 0, 0]], (3, 1), 7))
    
    def test_is_safe_not_on_row(self):
        self.assertFalse(is_safe([[1, 3, 5, 7, 9], [2, 4, 6, 8, 0]], (3, 1), 8))

    def test_is_safe_on_column(self):
        self.assertTrue(is_safe([[1, 3, 5, 7, 9], [2, 4, 6, 0, 0]], (3, 1), 8))
        
    def test_is_safe_on_row(self):
        self.assertTrue(is_safe([[1, 3, 5, 7, 9], [2, 4, 6, 8, 0]], (3, 1), 9))  

    def test_is_safe_on_block_1(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (2, 1), 1))
    
    def test_is_safe_on_block_2(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (4, 1), 3))
    
    def test_is_safe_on_block_3(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (7, 1), 1))
    
    def test_is_safe_on_block_4(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (1, 4), 1))
    
    def test_is_safe_on_block_5(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (3, 3), 6))

    def test_is_safe_on_block_6(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (7, 4), 1))
    
    def test_is_safe_on_block_7(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (1, 7), 1))
    
    def test_is_safe_on_block_8(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (4, 7), 2))

    def test_is_safe_on_block_9(self):
        self.assertTrue(is_safe(self.unfinished_sudoku, (8, 6), 9))

    # Utility functions

    @property
    def finished_sudoku(self):
        return [[2, 9, 6, 3, 1, 8, 5, 7, 4],
                [5, 8, 4, 9, 7, 2, 6, 1, 3],
                [7, 1, 3, 6, 4, 5, 2, 8, 9],
                [6, 2, 5, 8, 9, 7, 3, 4, 1],
                [9, 3, 1, 4, 2, 6, 8, 5, 7],
                [4, 7, 8, 5, 3, 1, 9, 2, 6],
                [1, 6, 7, 2, 5, 3, 4, 9, 8],
                [8, 5, 9, 7, 6, 4, 1, 3, 2],
                [3, 4, 2, 1, 8, 9, 7, 6, 5]]

    @property
    def unfinished_sudoku(self):
        return [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]]    

    @property
    def unsolvable_sudoku(self):
        return [[5, 0, 6, 5, 0, 8, 4, 0, 3],
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
