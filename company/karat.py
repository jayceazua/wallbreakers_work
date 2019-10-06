"""
Given a board and an end position for the player, write a function to determine if it is possible to travel from every open cell on the board to the given end position.

board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

board2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
]

board3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

board4 = [
    [0,  0,  0,  0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0,  0,  0,  0, 0],
]

end1 = (0, 0)
end2 = (5, 0)

Expected output:

isReachable(board1, end1) -> True
isReachable(board1, end2) -> True
isReachable(board2, end1) -> False
isReachable(board3, end1) -> False
isReachable(board4, end1) -> True

n: width of the input board
m: height of the input board
"""


board1 = [
    [0,  0,  0, 0, -1],
    [0, -1, -1, 0,  0],
    [0,  0,  0, 0,  0],
    [0, -1,  0, 0,  0],
    [0,  0,  0, 0,  0],
    [0,  0,  0, 0,  0],
]

board2 = [
    [0,  0,  0, 0, -1],
    [0, -1, -1, 0,  0],
    [0,  0,  0, 0,  0],
    [-1, -1,  0, 0,  0],
    [0, -1,  0, 0,  0],
    [0, -1,  0, 0,  0],
]

board3 = [
    [0,  0,  0,  0,  0,  0, 0],
    [0, -1, -1, -1, -1, -1, 0],
    [0, -1,  0,  0,  0, -1, 0],
    [0, -1,  0,  0,  0, -1, 0],
    [0, -1,  0,  0,  0, -1, 0],
    [0, -1, -1, -1, -1, -1, 0],
    [0,  0,  0,  0,  0,  0, 0],
]

board4 = [
    [0,  0,  0,  0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0,  0,  0,  0, 0],
]

end1 = (0, 0)
end2 = (5, 0)


def is_reachable(board, end):
    pass


# get all open positions
def all_open_positions(board):
    """
    return list of tuples of cooridinates
    """
    open_positions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                open_positions.append((i, j))
    return open_positions


def find_legal_moves(board, start_position):
    answer = []

    if start_position[0] != 0:
        top = board[start_position[0] - 1][start_position[1]]
        if top == 0:
            answer.append((start_position[0] - 1, start_position[1]))

    if start_position[0] != (len(board) - 1):
        bottom = board[start_position[0] + 1][start_position[1]]
        if bottom == 0:
            answer.append((start_position[0] + 1, start_position[1]))

    if start_position[1] != len(board[start_position[0]]) - 1:
        right = board[start_position[0]][start_position[1] + 1]
        if right == 0:
            answer.append((start_position[0], start_position[1] + 1))

    if start_position[1] != 0:
        left = board[start_position[0]][start_position[1] - 1]
        if left == 0:
            answer.append((start_position[0], start_position[1] - 1))

    return answer


# test helper function
print(all_open_positions(board1))


#  Driver Code
if __name__ == "__main__":
    #     generate all open positions
    open_positions = all_open_positions(board1)

#     print(find_legal_moves(board, start1))
#     print(find_legal_moves(board, start2))
#     print(find_legal_moves(board, start3))
#     print(find_legal_moves(board, start4))
#     print(find_legal_moves(board, start5))
#     print(find_legal_moves(board, start6))
#     print(find_legal_moves(board, start7))
