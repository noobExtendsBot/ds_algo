"""
Problem Link: https://leetcode.com/problems/group-anagrams/description/
"""


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        
        map_strs = defaultdict(list)
        res = list()
        for s in strs:
            
            map_strs[''.join(sorted(s))].append(s)
        # print(map_strs)
        for k,v in map_strs.items():
            res.append(v)
        # print(res)
        return res
        

