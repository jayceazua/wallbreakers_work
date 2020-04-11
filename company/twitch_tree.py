r"""
Reconstruct a binary tree using in-order and pre-order results

Input:
  in-order -> [10, 30, 40, 50, 60, 70, 90]
  pre-porder -> [50, 30, 10, 40, 70, 60, 90]

Output:

       50 <- Node Objects
     /   \
   30     70
 /   \   /   \
10   40 60   90


"""


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None
    


  def buildTree(preorder, inorder):
      # base case
      if not inorder:
          return

      # could use deque for O(1) operation on popping left
      index = inorder.index(preorder.pop(0))
      root = TreeNode(inorder[index])  # get the value
      # left branch -
      root.left = self.buildTree(preorder, inorder[0: index])
      # right branch -
      root.right = self.buildTree(preorder, inorder[index + 1:])
      # once we break the problem down to the smallest form we return that root node
      return root
