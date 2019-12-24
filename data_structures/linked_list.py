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



if __name__ == "__main__":
  ll = LinkedList()
  ll.insert_at_head(1)
  ll.insert_at_head(2)
  ll.insert_at_head(3)
  ll.insert_at_head(4)
  ll.insert_at_head(78)
  ll.insert_at_head(34)
  ll.insert_at_head(343)
  print("The size of the linked list should be 7:", ll.size)
  result = "head -> "
  current = ll.head
  while current:
    result += f"{ {current.data} } -> "
    current = current.get_next_node()
  result += "null"
  print(result)
