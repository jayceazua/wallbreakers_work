class HashEntry:
    def __init__(self, key, data):
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots

    # Hash Function
    def get_index(self, key):
        # hash is a built in function in Python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0
