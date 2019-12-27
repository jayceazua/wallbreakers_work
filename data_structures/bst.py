from bst_node import Node


class BST:
    def __init__(self):
        self.root = None

  # insert
  def insert(self, data):
    def insert_node(data, current):
      if data >= current.data:
        # right
        if not current.right:
          current.right = Node(data)
        else:
          insert_node(data, current.right)
      else:
        # left
        if not current.left:
          current.left = Node(data)
        else:
          insert_node(data, current.left)
    if not self.root:
      self.root = Node(data)
    else:
      insert_node(data, self.root)


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
