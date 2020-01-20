class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, val):
        current = self
        parent = None

        while current:
            parent = current
            if val < current.val:  # if val is less than the current node's val move to the left sub tree
                current = current.left
            else:  # move to the right
                current = current.right
        if not parent:
            parent = Node(val)
        elif val < parent.val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)

    def search(self, val):
        current = self

        while current:
            if val < current.val:
                currnet = current.left
            elif val > current.val:
                current = current.right
            elif val == current.val:
                return True
        return False


def buildTree(inOrder, preOrder, inStrt, inEnd):

    if (inStrt > inEnd):
        return None

    # Pich current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    # If this node has no children then return
    if inStrt == inEnd:
        return tNode

    # Else find the index of this node in Inorder traversal
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)

    # Using index in Inorder Traversal, construct left
    # and right subtrees
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

    return tNode


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i
# the 5 whys
#  - 
