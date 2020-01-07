"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


def swapPairs(head):
    if not head or head.next:
        return head
    # nodes to be swapped
    first = head
    second = head.next

    # swapping
    first.next = swapPairs(second.next)
    second.next = first

    # now head is second node
    return second
