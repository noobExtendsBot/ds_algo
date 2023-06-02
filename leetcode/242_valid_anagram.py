"""
Problem Link: https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity O(n)
        hash_s = [0]*26
        hash_t = [0]*26

        for i in s:
            hash_s[ord(i)-97] += 1

        for i in t:
            hash_t[ord(i)-97] += 1

        return hash_s == hash_t