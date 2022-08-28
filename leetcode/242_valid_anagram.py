"""
Problem Link: https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = [0 for i in range(200)]
        map_t = [0 for i in range(200)]

        for i in s:
            map_s[ord(i)] += 1
        for i in t:
            map_t[ord(i)] += 1

        return map_s == map_t
