from heapq import nlargest
"""
# connect levels of binary tree
#       1                   1              
#      /  \               /  \
#     2 -> 5             2 -> 5
#    / \    \           /  \    \
#   3 ->4     6        3 -> 4 -> 6

class Node:
    left: Node
    right: Node
    next: Node = None

"""
from collections import deque


def setNext(root: Node) -> None:
    if not root:
        return

    queue = deque()
    queue.append(root)  # 2, 5

    while queue:

        level = queue  # 5
        queue.clear()
        # while queue:
        #     level.append(queue.popleft())

        while level:

            current = level.popleft()  # proper way

            if level:  # assigns to right sibling
                current.next = level[0]

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


# select kth largest element
#        [2, 3, 4, 5, 6, 29, 18] -> len(arr) - 1
            pos = n - k

#               |
# list = [2, 3, 6, 18, 29, 4, 5]
# k = 1, return 18


def selectKth(list: List[int], k: int) -> int:
    return heapq.nlargest(k, List)[-1]
