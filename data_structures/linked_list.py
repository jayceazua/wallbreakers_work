from linked_list_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        # size of the linked list
        self.length = 0
        # properties for a doubly linked list
        self.tail = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        result = ""
        current = ll.head
        while current:
            result += f"<- { {current.data} } -> "
            current = current.next
        result += ""
        return result

    # inserting a new node at the head
    def insert_at_head(self, data):
        """
          Inserting a new node at the head of the linked list is an O(1) operation.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    # inserting a new node at the tail
    def insert_at_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        elif self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def insert(self, data):
        """
            This insert method inserts elements in an ascending sorting manner.
        """

        if not self.head or self.head.data >= data:
            self.insert_at_head(data)
        elif self.tail.data <= data:
            self.insert_at_tail(data)
        else:
            new_node = Node(data)
            current = self.head
            self.length += 1
            while current.next:
                if current.next.data >= data:
                    # insert at the current position
                    current.next.prev, new_node.next = new_node, current.next
                    new_node.prev, current.next = current, new_node
                    break
                current = current.next

    # deleting a node at the head

    def delete_head(self):
        """
          Deleting a node from the head of the linked list is an O(1) operation.
            It is good to note that by simply referencing to the old head's next node it delete its, 
              and it gets picked up by the language's garbage collector.
        """
        self.head = self.head.next
        self.length -= 1

    # searching for a specific node
    def find(self, data):
        """
          This method takes O(n) time to search through the linked list.
          Could be used to eliminate adding duplicates into the linked list.
        """
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(8)
    ll.insert(1)
    ll.insert(7)
    ll.insert(5)
    ll.insert(2)
    ll.insert(3)
    ll.insert(9)
    ll.insert(0)
    ll.insert(6)
    ll.insert(4)
    print(f"Search for 7 in the linked list, is it there? {ll.find(7)}")
    print(f"Search for 5 in the linked list, is it there? {ll.find(5)}")
    print("The size of the linked list should be 6:", ll.length)
    print(ll)

    # reversed.
    current = ll.tail
    while current:
        print(f"<- { {current.data} } ->", end=" ")
        current = current.prev
