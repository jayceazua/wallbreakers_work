# connect levels of binary tree
#       1                   1
#      /  \               /  \
#     2 -> 5             2 -> 5
#    / \    \           /  \    \
#   3 ->4     6        3 -> 4 -> 6
# https: // leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/
from heapq import nlargest
from collections import deque


class Node:
    left: Node
    right: Node
    next: Node = None


def setNext(root):
    if not root:
        return

    queue = deque()
    queue.append(root)  # 2, 5

    while queue:

        level = queue.copy()  # 5
        queue.clear()

        # while queue:
        #     level.append(queue.popleft())

        while level:

            current = level.popleft()  # 2

            if level:  # assigns to right sibling
                current.next = level[0]

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


# select kth largest element
#        [2, 3, 4, 5, 6, 29, 18] -> len(arr) - 1
            # pos = n - k
#               | -> quickSelection
# list = [2, 3, 6, 18, 29, 4, 5]
# k = 1, return 18

# https://leetcode.com/problems/kth-largest-element-in-an-array/


def selectKth(l, k):
    return nlargest(k, l)[-1]  # O(n log k)
