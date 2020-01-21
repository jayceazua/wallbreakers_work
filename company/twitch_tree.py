r"""
Leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


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


def buildTree(preorder, inorder):

    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])

        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root
