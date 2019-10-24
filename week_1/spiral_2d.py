"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []

        if len(matrix) == 0:
            return results

        # create matrix boundaries
        # top
        row_begin = 0
        # left
        column_begin = 0
        # bottom
        row_end = len(matrix) - 1
        # right
        column_end = len(matrix[0]) - 1

        while row_begin <= row_end and column_begin <= column_end:
            # left to right
            for i in range(column_begin, column_end + 1):
                results.append(matrix[row_begin][i])

            row_begin += 1

        # top to the bottom
            for i in range(row_begin, row_end + 1):
                results.append(matrix[i][column_end])

            column_end -= 1

        # right to left
            if row_begin <= row_end:
                for i in range(column_end, column_begin-1, -1):
                    results.append(matrix[row_end][i])

            row_end -= 1

        # bottom to the top before 0,0 coordinate
            if column_begin <= column_end:
                for i in range(row_end, row_begin-1, -1):

                    results.append(matrix[i][column_begin])

            column_begin += 1

        return results
