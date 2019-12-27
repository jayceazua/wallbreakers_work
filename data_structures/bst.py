from bst_node import Node

class BST:
    def __init__(self):
        self.root = None

  # insert
  # delete
  # search
    def find(self, data):
        def search(data, current):
            if data == current.data:
                return root
            # move left
            if current and data < current.data:
                return search(data, current.left)
            # move right
            elif current:
                return search(data, current.right)
            # if nothing is round
            return None

        return search(data, self.root)

  # in-order
  # post-order
  # pre-order
  # level-order
