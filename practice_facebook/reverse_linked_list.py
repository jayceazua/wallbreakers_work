"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


def reverseList(head):
    #         if head == None or head.next == None:
    #             return head

    #         p = self.reverseList(head.next)
    #         head.next.next = head
    #         head.next = None
    #         return p

    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
