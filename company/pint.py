"""
Given a 2D array of letters, find the longest path that you can create by moving between adjacent letters in the alphabet.
For example, if you are on a D, you may move to an E or a C. You may move up, down, left, or right by a single row or column, 
but not diagonally or move more than one space. You may start at any square, and you may only use a given row/column pair once.

Return an ordered list of row/column pairs that represents the longest path. 
If there is a tie between two paths, return the one that starts with the lowest row index, 
and if that is also a tie, use the one with the lowest row and column indices.
(If there is still a tie, returning either path is acceptable.)
Example 1:
    input:
    [
        ['A', 'B', 'H', 'F'],
        ['C', 'C', 'D', 'G'],
        ['A', 'B', 'D', 'F']
    ]

    output:
        'ABCBA'

Example 2:
    input:
    [
        ['L', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'J'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    ]
    output:
        'JIHGFEDCBA'

Example 3:
    input:
    [
        ['A', 'B'],
        ['B','A']
    ]
    output:
        'ABAB'

Example 4:
    input:
    [
        ['C', 'B', 'H', 'F'],
        ['C', 'C', 'D', 'G'],
        ['A', 'B', 'D', 'F'],
    ]
    output:
        'CBCBA'
"""
