from queue import Queue
# light weight -> doc: https://docs.python.org/3/library/asyncio-queue.html
from queue import Queue
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}


class Graph:
    def __init__(self, edges=None):
        self.graph = {}

        # add edges if they are given (as a list of tuples)
        if edges:
            for start, end in edges:
                self.add_edge(start, end)

    def add_edge(self, start, end):
        self.graph.setdefault(start, []).append(end)

    def print_all_paths(self, start, end, curr_path=None, seen=None):
        # on the first iteration create curr_path array and seen set
        if not curr_path:
            curr_path = []
            seen = set()

        seen.add(start)
        curr_path.append(start)

        # base case
        # when the start is the end, print the path
        if start == end:
            print(', '.join(map(str, curr_path)))

        # every other case
        else:
            # recurse on all unseen paths
            for neighbor in self.graph[start]:
                if neighbor not in seen:
                    self.print_all_paths(neighbor, end, curr_path, seen)

        # remove start from seen and curr path
        seen.remove(start)
        curr_path.pop()


if __name__ == '__main__':
    edges = [
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('A', 'C'),
        ('A', 'D'),
    ]

    g = Graph(edges)

    g.print_all_paths('A', 'D')


####
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# shortest path

def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)


"""
g = graph: hash-map representation of a graph 
s = source: string
d = destination: string
"""


def has_path_dfs(g, s, d, seen=None):  # dfs/ stack
    if seen is None:  # dealing with python's pointer issue
        seen = set()

    # base case
    if s == d:  # path is found
        return True

    # get neighbors and recurse the has_path function
    for neighbor in next_move_dfs(g, s, seen):  # next move
        seen.add(neighbor)
        # if any of the neighbors has a path
        is_path_found = has_path_dfs(g, neighbor, d, seen)

        if is_path_found:
            return True

    return False


def next_move_dfs(g, s, seen):
    return (n for n in g[s] if n not in seen)


# from collections import deque -> heavy
# q = Queue()
# q.put()
# q.get()


def has_path_bfs(graph, source, distination):

    seen = set()  # step 1
    queue = Queue()  # step 2
    queue.put(source)

    while not queue.empty():
        current_move = queue.get()
        # check if the current move is the distination
        if current_move == distination:
            return True

        seen.add(current_move)  # add the current move to the queue

        # get all the neighbors of the current move
        for neighbor in next_moves_bfs(graph, current_move, seen):  # step 3
            queue.put(neighbor)

    return False


def next_moves_bfs(graph, current_move, seen):
    # iterable of all possible next moves of the current vertex we are visiting
    return (move for move in graph[current_move] if move not in seen)


source = 'A'
distination = 'E'
# print("Has Path bfs:", has_path_bfs(graph, source, distination))

####### shortest path


def shortest_path_bfs(g, source, distination):  # O(V + E)

    queue = Queue()  # component 1
    queue.put((source, []))

    seen = set()  # component 2

    while not queue.empty():

        current_move, current_path = queue.get()
        current_path = current_path + [current_move]

        seen.add(current_move)

        if current_move == distination:
            return current_path

        # Component 3
        for neighbor in next_moves_shortest_path(g, current_move, seen):
            queue.put((neighbor, current_path))

    return []


def next_moves_shortest_path(g, current_move, seen):
    # generator -> better memory efficient
    return (n for n in g[current_move] if n not in seen)


# https://pathfinding-visualizer.netlify.app
# https://jshams.github.io/sliding-puzzle/frontend/


s = 'A'
d = 'B'
# print(shortest_path_bfs(graph, s, d))


matrix = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]


# up, right, down, left
def shortest_path_matrix(m, start, end):
    '''
    m - 2d matrix
    start - integer tuple (1, 2)
    end - integer tuple
    '''

    queue = Queue()  # component 1
    queue.put((start, []))

    seen = set()  # component 2

    while not queue.empty():

        curr_move, current_path = queue.get()

        current_path = current_path + [curr_move]

        seen.add(curr_move)

        if curr_move == end:
            return current_path

        for move in next_moves(m, curr_move, seen):  # Component 3
            queue.put((move, current_path))

    return "No path found"


def next_moves(m, curr_move, seen):  # used for movable directions (N, S, E, W)

    r, c = curr_move
    row = len(m)
    col = len(m[0])

    # bound checking
    possible_moves = []

    # move down?
    if r < row - 1:  # true you can move down
        possible_moves.append((r + 1, c))
    # move up?
    if r > 0:
        possible_moves.append((r - 1, c))
    # move right?
    if c < col - 1:
        possible_moves.append((r, c + 1))
    # move left?
    if c > 0:
        possible_moves.append((r, c - 1))

    moves = []
    # filter moves based on these conditions: is it in seen and is it land?
    for move in possible_moves:
        pr, pc = move
        if m[pr][pc] == 1 and move not in seen:
            moves.append(move)

    return moves

# if __name__ == '__main__':

#     ans = shortest_path_matrix(matrix, (0, 0), (3, 2))
#     print(ans)


class Node:  # creates our doubly linked list
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.next = None
        self.prev = None


class LRU_cache:
    def __init__(self, capacity):
        self.capacity = capacity

        self.lookup = dict()

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def setter(self, key, value):
        n = Node(key, value)

        self._add(n)

        self.lookup[key] = n

        if len(self.lookup) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.lookup[n.key]

    def getter(self, key):
        if key in self.lookup:
            n = self.lookup[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1  # or return to the user a message "Key is not found"


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
            if board[row][col] == '0':
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
    if c < colLength - 1:
        possible_moves.append((r, c + 1))
    # left
    if c > 0:
        possible_moves.append((r, c - 1))

    moves = []

    for move in possible_moves:
        pr, pc = move
        if board[pr][pc] == '0' and move not in seen:
            moves.append(move)
    return moves


if __name__ == "__main__":
    # board 1
    print(find_exit(board_1, start_1_1))  # => (5,2)
    print(find_exit(board_1, start_1_2))
    print(find_exit(board_1, start_1_3))
    print(find_exit(board_1, start_1_4))
    # board 2
    print(find_exit(board_2, start_2_1))
    print(find_exit(board_2, start_2_2))
    # board 3
    print(find_exit(board_3, start_3_1))
    print(find_exit(board_3, start_3_2))
    print(find_exit(board_3, start_3_3))
    print(find_exit(board_3, start_3_4))
    # board 4
    print(find_exit(board_4, start_4_1))
    print(find_exit(board_4, start_4_2))
    print(find_exit(board_4, start_4_3))
    print(find_exit(board_4, start_4_4))
    # board 5
    print(find_exit(board_5, start_5_1))
    print(find_exit(board_5, start_5_2))


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
