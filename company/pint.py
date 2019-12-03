"""
Given a 2D array of letters, find the longest path that you can create by moving between adjacent 
letters in the alphabet - for example, if you are on a D, you may move to an E or a C. 
You may move up, down, left, or right by a single row or column, but not diagonally 
or move more than one space. You may start at any square, and you may only use a given row/column pair once.

Return an ordered list of row/column pairs that represents the longest path. 
If there is a tie between two paths, return the one that starts with the lowest row index, 
and if that is also a tie, use the one with the lowest row and column indices.
(If there is still a tie, returning either path is acceptable.)


------
Clarificatiions:
 - The array will always contain at least one value.
 - All lines will contain the same number of letters.
 - A and Z are not considered 'adjacent' letters.
 - If no solution is present what should we return?
 - What are we optimizing for; space or time complexity?
 - Can I create extra space?
 - Is it a perfect square?
 - Will it only contain letters; any special chars, numbers, etc?
 - Does case matter?
 - Will there be lowercase as well?
 - If we see a Letter can we move to the same letter? - No!
 

jayce ->
    longest path-> some type of graph algorithm: bfs -> shortest
    letter with ascii -1 and +1
    only up, down, right, left -> dfs/ bfs
    move only one at a time
    start any position
    checked for visited positions
    
    ordered list of row/col [(row, col),(row, col),(row, col)]
    lowest row index; 0 is the lowest row index (starting from the top)
    both low; then check for column index (far left) lowest col is 0
    if still tie either path is okay
    
    

erik's Restating:
    INPUT: Matrix
    Given a matrix, find the longest path can create by using the previous or next character in the alphabet.

    You can move up any direction but not across.

    You can only move one space at a time.

    * you can only use the given array and not create any duplicates.

    -> RETURN:





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
        'CBCBA' -> [(0,0), (0,1), (1,1), (2,1), (2,0)]
        
        
        
-Solution samples-

    we cannot go to a previous visited node
    we keep track of the path we have visited...
    keep track the number of moves we made...
    continue checking if we have visited the position
    
    


https://realpython.com/python-thinking-recursively/
"""

# we are using depth-first search here...


def dfs(grid, row, col, visited, moves):
    """
    We return two things; max moves and max path.
    """
    m = len(grid)
    n = len(grid[0])

    # we have reached the end
    if row < 0 or col < 0 or row >= m or col >= n or (row, col) in visited:
        return (moves, visited)

    # add to the visited
    visited.append(grid[row][col])
    moves += 1

    # check up
    if abs(ord(grid[row][col]) - ord(grid[row - 1][col])) == 1:
        dfs(grid, row - 1, col, visited, moves)

    # check down
    if abs(ord(grid[row][col]) - ord(grid[row + 1][col])) == 1:
        dfs(grid, row + 1, col, visited, moves)

    # check right
    if abs(ord(grid[row][col]) - ord(grid[row][col + 1])) == 1:
        dfs(grid, row, col + 1, visited, moves)

    # check left
    if abs(ord(grid[row][col]) - ord(grid[row][col - 1])) == 1:
        dfs(grid, row, col - 1, visited, moves)
    # get the max path between all four possible paths


def bfs(grid, row, col):
    # up, down, right, left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = [(row, col)]
    visited = set()
    visited.add((row, col))
    # find all possible paths
    paths = []
    while q:
        i, j = q.pop(0)

        for index, d in enumerate(directions):
            r, c = i + d[0], j + d[1]

            # check boundaries and check if it is possible to move
            if check_boundaries(grid, r, c) or (r, c) in visited or abs(ord(grid[r][c]) - ord(grid[i][j])) != 1:
                continue
            # add to the path...
            paths.append([(row, col), (r, c)])
            q.append((r, c))
            visited.add((r, c))
    # with all possible paths ge the longest one
    return paths


def check_boundaries(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])

    if r < 0 or c < 0 or r >= rows or c >= cols:
        return True
    return False


def we_say_hey(grid):

    rows = len(grid)
    cols = len(grid[0])

    max_moves = float('-inf')
    longest_path = set()
    # pathss = []
    # here...
    for row in range(rows):  # O(r * c)
        for col in range(cols):

            # if there is a path we already know the path along so we check if it is in the current longest path to prevent
                # checking something more than once...
            if (row, col) not in longest_path:
                paths = bfs(grid, row, col)

    # return sorted(longest_path, key=lambda x: (x[0], x[1]))
    return longest_path


grid = [
    ['C', 'B', 'H', 'F'],
    ['C', 'C', 'D', 'G'],
    ['A', 'B', 'D', 'F'],
]
we_say_hey(grid)


"""
Different Paths:

    [    
        [(0, 0), (0, 1)], 
        [(0, 0), (1, 1)], 
        [(0, 0), (1, 2)],
        [(0, 0), (2, 1)],
        [(0, 0), (2, 0)],
    ]
    
"""
