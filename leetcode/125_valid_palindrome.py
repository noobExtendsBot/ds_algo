"""
Problem Link: https://leetcode.com/problems/valid-palindrome/
"""
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        dq = deque(s)
        while len(dq)>1:
            if dq.popleft() != dq.pop():
                return False
        return True
