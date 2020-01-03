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
