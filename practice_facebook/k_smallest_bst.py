"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


# you could also use a minheap which would be a total of O(n log n) to create


# inorder traversal without recursion
def kthSmallest(root, k):
    if not root:
        return None

    stack = []

    while True:
        while root:
            # append all the left nodes of the tree into the stack
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1  # subtract 1 of k
        if not k:  # when k equals 0
            return root.val  # return the value of the kth value
        root = root.right  # else continue moving to the right


# use recursively the inorder traversal
# def kthSmallest(root, k):
#   nums = [0]*2
#   inorder(root, nums, k)
#   return nums[1]

# def inorder(root, nums, k):
#   if not root:
#     return

#   inorder(root.left, nums, k)
#   nums += 1
#   if nums[0] == k:
#     nums[1] = root.val
#     return
#   inorder(root.right, nums, k)
