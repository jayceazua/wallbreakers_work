from linked_list_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        # size of the linked list
        self.size = 0

    # inserting a new node
    def insert_at_head(self, data):
        """
          Inserting a new node at the head of the linked list is an O(1) operation.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

        self.size += 1

    def insert_tail(self, data):
        pass

    def insert_specific(self, data):
        pass

    # deleting a node
    # searching for a node
