"""
Problem Link: https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(200)
        map_s = [0 for i in range(200)]
        map_t = [0 for i in range(200)]

        for i in s:
            map_s[ord(i)] += 1
        for i in t:
            map_t[ord(i)] += 1

        return map_s == map_t

        # another solution without any extra space
        # Time Complexity: O(n)
        # Space Complexity: O(26)
        # if len(s) != len(t):
        #     return False
        
        # map_s, map_t = {}, {}
        # for i in range(len(s)): 
        #     map_s[s[i]] = 1 + map_s.get(s[i], 0)
        #     map_t[t[i]] = 1+ map_t.get(t[i], 0)
        
        # return map_s == map_t