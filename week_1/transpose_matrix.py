"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        temp = []
        new_matrix = []

        matrix = A  # make a reference

        # since it is on its main diagonal  (0,0) -> (1, 0) ...(0, n-1)
        row_index = 0
        column_index = 0

        row_length = len(matrix)
        column_length = len(matrix[0])

        # is the matrix a perfect square?

        # assuming the matrix is a perfect - solution

        while column_index < column_length:

            while row_index < row_length:

                temp.append(matrix[row_index][column_index])
                row_index += 1

            new_matrix.append(temp)
            temp = []
            row_index = 0
            column_index += 1

        return new_matrix
