"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0

        # BFS - level order
        queue = deque()
        queue.append(root)

        while queue:
            current = queue.popleft()

            if current and current.left:
                # check if it is a leaf
                if not current.left.left and not current.left.right:
                    total += current.left.val
                else:
                    queue.append(current.left)

            if current and current.right:
                queue.append(current.right)

        return total
