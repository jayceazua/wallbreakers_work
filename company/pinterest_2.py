# We have a two-dimensional board game involving snakes.  The board has two types of squares on it: +'s represent impassable squares where snakes cannot go, and 0's represent squares through which snakes can move.

# Snakes may move in any of four directions - up, down, left, or right - one square at a time, but they will never return to a square that they've already visited.  If a snake enters the board on an edge square, we want to catch it at a different exit square on the board's edge.

# The snake is familiar with the board and will take the route to the nearest reachable exit, in terms of the number of squares it has to move through to get there. Note that there may not be a reachable exit.

# Here is an example board:

#     col-->        0  1  2  3  4  5  6  7  8
#                +---------------------------
#     row      0 |  +  +  +  +  +  +  +  0  0
#      |       1 |  +  +  0  0  0  0  0  +  +
#      |       2 |  0  0  0  0  0  +  +  0  +
#      v       3 |  +  +  0  +  +  +  +  0  0
#              4 |  +  +  0  0  0  0  0  0  +
#              5 |  +  +  0  +  +  0  +  0  +

# Write a function that takes a rectangular board with only +'s and O's, along with a starting point on the edge of the board, and returns the coordinates of the nearest exit to which it can travel.  If there is a tie, return any of the nearest exits.

# Complexity Analysis:

# r: number of rows in the board
# c: number of columns in the board

from queue import Queue
board_1 = [['+', '+', '+', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '+', '+'],
           ['0', '0', '0', '0', '0', '+', '+', '0', '+'],
           ['+', '+', '0', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '0', '+'],
           ['+', '+', '0', '+', '+', '0', '+', '0', '+']]

start_1_1 = (2, 0)  # Expected output = (5, 2)
start_1_2 = (0, 7)  # Expected output = (0, 8)
start_1_3 = (5, 2)  # Expected output = (2, 0) or (5, 5)
start_1_4 = (5, 5)  # Expected output = (5, 7)

board_2 = [['+', '+', '+', '+', '+', '+', '+'],
           ['0', '0', '0', '0', '+', '0', '+'],
           ['+', '0', '+', '0', '+', '0', '0'],
           ['+', '0', '0', '0', '+', '+', '+'],
           ['+', '+', '+', '+', '+', '+', '+']]


# Expected output = null (or a special value representing no possible exit)
start_2_1 = (1, 0)
start_2_2 = (2, 6)  # Expected output = null

board_3 = [['+', '0', '+', '0', '+', ],
           ['0', '0', '+', '0', '0', ],
           ['+', '0', '+', '0', '+', ],
           ['0', '0', '+', '0', '0', ],
           ['+', '0', '+', '0', '+']]

start_3_1 = (0, 1)  # Expected output = (1, 0)
start_3_2 = (4, 1)  # Expected output = (3, 0)
start_3_3 = (0, 3)  # Expected output = (1, 4)
start_3_4 = (4, 3)  # Expected output = (3, 4)

board_4 = [['+', '0', '+', '0', '+', ],
           ['0', '0', '0', '0', '0', ],
           ['+', '+', '+', '+', '+', ],
           ['0', '0', '0', '0', '0', ],
           ['+', '0', '+', '0', '+']]

start_4_1 = (1, 0)  # Expected output = (0, 1)
start_4_2 = (1, 4)  # Expected output = (0, 3)
start_4_3 = (3, 0)  # Expected output = (4, 1)
start_4_4 = (3, 4)  # Expected output = (4, 3)

board_5 = [['+', '0', '0', '0', '+', ],
           ['+', '0', '+', '0', '+', ],
           ['+', '0', '0', '0', '+', ],
           ['+', '0', '+', '0', '+']]

start_5_1 = (0, 1)  # Expected output = (0, 2)
start_5_2 = (3, 1)  # Expected output = (0, 1)


def find_exit(board, start):
    seen = set()
    queue = Queue()
    queue.put((start))

    bounds = get_board_bounds(board)  # O(n^ 2) runtime

    while not queue.empty():
        current_move = queue.get()
        seen.add(current_move)

        r, c = current_move
        cell_value = board[r][c]

        if cell_value == "0":
            if current_move != start and current_move in bounds:  # has hit a bound that is not the start
                return current_move
            # get next moves possible
            for move in next_moves(board, current_move, seen):
                queue.put(move)
    return None


def get_board_bounds(board) -> bool:
    bounds = set()
    rowLength = len(board)

    for row in range(rowLength):
        colLength = len(board[row])
        for col in range(colLength):
            if row == 0:
                bounds.add((row, col))
            if row == rowLength - 1:
                bounds.add((row, col))

            if col == 0:
                bounds.add((row, col))

            if col == colLength - 1:
                bounds.add((row, col))
    return bounds


def next_moves(board, current_move, seen):
    r, c = current_move
    rowLength = len(board)
    colLength = len(board[r])

    possible_moves = []
    # down
    if r < rowLength - 1:
        possible_moves.append((r + 1, c))
    # up
    if r > 0:
        possible_moves.append((r - 1, c))
    # right
    if c < colLength:
        possible_moves.append((r, c + 1))
    # left
    if c > 0:
        possible_moves.append((r, c - 1))

    moves = []

    for move in possible_moves:
        pr, pc = move

        if board[pr][pc] == "0" and move not in seen:
            moves.append(move)
    return moves


if __name__ == "__main__":
    print(find_exit(board_1, (2, 0)))  # => (5,2)


# def find_passable_lanes(board):
#     if not board:
#         return ([],[])


#     rows_cols = ([],[]) # O(rc) space

#     rowLength = len(board)
#     colsLength = len(board[0])


#     for i in range(rowLength): # O(rc) runtime
#         cell_value = board[i][0]
#         if cell_value == "0":
#             if is_passthrough_rows(board, i, 0):
#                 rows_cols[0].append(i)


#     for j in range(colsLength): # O(cr) runtime
#         cell_value = board[0][j]
#         if cell_value == "0":
#             if is_passthrough_cols(board, 0, j):
#                 rows_cols[1].append(j)

#     return rows_cols


# def is_passthrough_cols(board, row, col) -> bool:
#     rowLength = len(board)

#     for r in range(rowLength):
#         cell_value = board[r][col]

#         if cell_value == "+":
#             return False
#     return True

# def is_passthrough_rows(board, row, col) -> bool:
#     colsLength = len(board[0])

#     for c in range(colsLength):
#         cell_value = board[row][c]

#         if cell_value == "+":
#             return False
#     return True
