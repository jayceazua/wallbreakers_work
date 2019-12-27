from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, item):
        self.items.insert_at_tail(item)

    def dequeue(self):
        return self.items.delete_head()

    def peek(self):
        return self.items.head

    def is_empty(self):
        return self.items.head == None

    def get_queue(self):
        return self.items
