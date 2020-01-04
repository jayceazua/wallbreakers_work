"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

from collections import deque


def isSameTree(p, q):
    def check(p, q):
        # both are none
        if not p and not q:
            return True
        # one of them is none
        if not q or not p:
            return False
        # the values do not equal
        if p.val != q.val:
            return False
        return True

    queue = deque([(p, q)])

    while queue:
        p, q = queue.popleft()
        if not check(p, q):
            return False

        if p:
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
    return True
