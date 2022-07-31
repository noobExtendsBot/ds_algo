"""
Problem Link: https://leetcode.com/problems/valid-palindrome/
"""
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_deque = deque([x.lower() for x in s if x.isalpha() or x.isdigit()])
        if len(my_deque) == 1:
            return True
        else:
            palindrome_match = True
            while len(my_deque) > 1 and palindrome_match:
                first = my_deque.pop()
                second = my_deque.popleft()
                if first != second:
                    palindrome_match = False
        return palindrome_match
