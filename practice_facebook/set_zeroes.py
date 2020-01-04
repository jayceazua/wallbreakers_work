"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    if not matrix:
        return matrix

    rows = set()
    cols = set()

    r = len(matrix)
    c = len(matrix[0])
    # find all zeros and store their rows and columns
    for i in range(r):  # O(m)
        for j in range(c):  # O(n)
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # if it is a row turn that entire vertical row into zeroes
    for row in rows:
        for col in range(c):
            matrix[row][col] = 0
    # if it is a column turn that entire horizontal column into zeroes
    for row in range(r):
        for col in cols:
            matrix[row][col] = 0
