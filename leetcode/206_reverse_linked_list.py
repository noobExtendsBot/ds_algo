"""
Problem Link: https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def reverseListUsingRecursion(
            self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node is None:
            return node

        if node.next is None:
            return node

        node1 = self.reverseList(node.next)
        previous = node.next
        previous.next = node
        node.next = None
        return node1
