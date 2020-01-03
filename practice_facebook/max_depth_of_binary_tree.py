"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def maxDepth(root):
    # iterative solution
    stack = []
    if root:
        stack.append((1, root))
    depth = 0
    while stack:
        current, root = stack.pop()
        if root:
            depth = max(depth, current)
            # left
            stack.append((current + 1, root.left))
            # right
            stack.append((current + 1, root.right))
    return depth

    # recursive solution
    # if not root:
    # return 0
    # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


"""
Engineering Trade-offs:
  - the recursive solution could run into a call stack overflow. O(n) runtime, worse case scenario if the tree is unbalanced space complexity could be O(n), best case scenario could be O(log n) if the tree is balanced.
  - using the iterative solution we prevent running into a call stack overflow, but it is the same for space complexity where worse case when the tree is unbalanced it will be O(n), best case is if the tree is balanced which would then be O(log n)
"""
