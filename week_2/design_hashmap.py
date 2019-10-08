"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap(object):

    def __init__(self, capacity=1001):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.hashMap = [None] * capacity

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.capacity
        node = self.hashMap[index]
        if node is None:
            self.hashMap[index] = ListNode(key, value)
            return
        pre = None
        while node:
            if node.key == key:
                node.val = value
                return
            pre = node
            node = node.next
        newNode = ListNode(key, value)
        pre.next = newNode

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.capacity
        node = self.hashMap[index]
        while node:
            #print(node.key)
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.capacity
        node = self.hashMap[index]
        if node and node.key == key:
            self.hashMap[key % self.capacity] = node.next
            return
        pre = None
        while node:
            if node.key == key:
                pre.next = node.next
                return
            pre = node
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
