"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_row_valid(row):
                return False

        # only go through one column at a time
        for column_index in range(0, 9):
            if not self.is_column_valid(board, column_index):
                return False

        # go through a 3x3 box
        for row_index in [0, 3, 6]:
            for column_index in [0, 3, 6]:
                if not self.is_box_valid(board, row_index, column_index):
                    return False
        return True

    # check row if valid

    def is_row_valid(self, row):
        # Ryan's implementation - good
        row = [num for num in row if num != "."]
        if len(row) != len(set(row)):
            return False
        return True

    # check column if valid

    def is_column_valid(self, board, column_index):
        seen = set()
        for row_index in range(0, 9):
            num = board[row_index][column_index]
            if num.isnumeric():
                if num in seen:
                    return False
                seen.add(num)
        return True

    # check 3x3 sub-boxes if valid
    def is_box_valid(self, board, row_top_left, column_top_left):
        seen = set()
        for row_offset in range(0, 3):
            for column_offset in range(0, 3):
                row_index = row_top_left + row_offset
                column_index = column_top_left + column_offset
                num = board[row_index][column_index]
                if num.isnumeric():
                    if num in seen:
                        return False
                    seen.add(num)
        return True
