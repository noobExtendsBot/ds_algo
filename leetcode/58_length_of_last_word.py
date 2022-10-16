"""
Problem Link: https://leetcode.com/problems/length-of-last-word/description/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        for i in s[::-1]:
            if i != " ":
                count += 1
            else:
                break
        return count
