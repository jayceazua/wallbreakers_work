from linked_list_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        # size of the linked list
        self.length = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
      result = "head -> "
      current = ll.head
      while current:
          result += f"{ {current.data} } -> "
          current = current.get_next_node()
      result += "null"
      return result

    # inserting a new node at the head
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
        self.length += 1

    # deleting a node at the head
    def delete_head(self):
        """
          Deleting a node from the head of the linked list is an O(1) operation.
            It is good to note that by simply referencing to the old head's next node it delete its, 
              and it gets picked up by the language's garbage collector.
        """
        self.head = self.head.get_next_node()
        self.length -= 1

    # searching for a node


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(1)
    ll.insert_at_head(2)
    ll.insert_at_head(3)
    ll.insert_at_head(4)
    ll.insert_at_head(5)
    ll.insert_at_head(6)
    ll.insert_at_head(7)
    ll.delete_head()
    print("The size of the linked list should be 6:", ll.length)
    print(ll)

