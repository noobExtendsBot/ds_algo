"""
Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def add_to_end(self, val):
        previous = None
        current = self.head

        while current is not None:
            previous = current
            current = current.next

        if previous is None:
            new_node = ListNode(val)
            self.head = new_node
        else:
            new_node = ListNode(val)
            previous.next = new_node


class Solution:
    def mergeTwoLists(
            self,
            list1: Optional[ListNode],
            list2: Optional[ListNode]) -> Optional[ListNode]:
        llist = LinkedList()

        while list1 is not None and list2 is not None:
            if list1.val == list2.val:
                llist.add_to_end(list1.val)
                llist.add_to_end(list2.val)
                list1 = list1.next
                list2 = list2.next
            elif list1.val > list2.val:
                llist.add_to_end(list2.val)
                list2 = list2.next
            elif list1.val < list2.val:
                llist.add_to_end(list1.val)
                list1 = list1.next

        if list1 is None and list2 is not None:
            while list2 is not None:
                llist.add_to_end(list2.val)
                list2 = list2.next
        else:
            while list1 is not None:
                llist.add_to_end(list1.val)
                list1 = list1.next
        return llist.head
