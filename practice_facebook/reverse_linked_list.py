"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


def reverseList(head):
    #         if not head or not head.next:
    #             return head

    #         p = reverseList(head.next)
    #         head.next.next = head
    #         head.next = None
    #         return p
    previous = None  # <- new reversed linked list
    current = head

    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    return previous
