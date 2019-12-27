from bst_node import Node


class BST:
    def __init__(self):
        self.root = None
  # insert

    def insert(self, data):
        """
        Best case: when binary tree is a completely balanced tree
        O(log n) runtime complexity
        """
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
  # search

    def find(self, data):
        """
        O(log n) worse case scenario
        """
        def search(data, current):
            if data == current.data:
                return current.data
            # move left
            if current and data < current.data:
                return search(data, current.left)
            # move right
            elif current:
                return search(data, current.right)
            # if nothing is round
            return None
        return search(data, self.root)

  # delete
    def delete(self, data):
        """
        O(log n) worse case scenario
        Case 1: node to be deleted is a leaf
        Case 2: node to be deleted has one child
        Case 3: node to be deleted has two children
        """
        if not self.find(data):
            return f"{data} is not in the binary search tree."
        # get a reference of the parent node
        current = self.root
        parent = self.root
        is_left_child = False

        if not current:
            return

        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
                is_left_child = True
            else:
                current = current.right
                is_left_child = False

        if not current:
            return

        # Case 1 - is a leaf
        if not current.left and not current.right:
            if current == self.root:
                self.root == None
            else:
                if is_left_child:
                    parent.left = None
                else:
                    parent.right = None
        # Case 2 - has one child
        elif not current.right:
            if current == self.root:
                self.root = self.root.left
            elif is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left

        elif not current.left:
            if current == self.root:
                self.root = self.root.right
            elif is_left_child:
                parent.left = current.right
            else:
                parent.right = current.right
        # Case 3 - has two children
            # find the node that is greater than the node to be deleted
            # but less than the greater node
            # find the successor node which is to the right of the node to be deleted but less than that node
            # bring the successor to the current node to be deleted,
            # make the left child of current node the left child of the successor node
            # then the right child of the current node is the right child of the successor node
            # then break the connection of the successor's parent
            # the current node's parent connection needs to connect to the current node's parent.
            # if the successor has a right child then the parent of the successor's left child becomes their left child...

    # in-order

    def in_order(self):
        pass
    # post-order

    def post_order(self):
        pass
    # pre-order

    def pre_order(self):
        pass
    # level-order

    def level_order(self):
        pass
    # height

    def height(self):
        pass

    def smallest_value(self):
        current = self.root
        if current:
            while True:
                if not current.left:
                    return current.data
                current = current.left

    def largest_value(self):
        current = self.root
        if current:
            while True:
                if not current.right:
                    return current.data
                current = current.right
