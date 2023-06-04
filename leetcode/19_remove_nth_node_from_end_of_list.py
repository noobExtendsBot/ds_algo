"""
Problem link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


class Solution:
    def get_size(self, head):
        current = head
        size = 0
        while current is not None:
            size += 1
            current = current.next
        return size

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = self.get_size(head)
        element_num = size - n + 1
        previous = None
        current = head
        count = 0
        if size == 1 and element_num == 1:
            return None
        elif element_num == 1:
            head = current.next
        else:
            while current is not None:
                count += 1
                if count == element_num:
                    previous.next = current.next
                    break
                previous = current
                current = current.next
        return head
