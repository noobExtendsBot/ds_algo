"""
Problem Link: https://leetcode.com/problems/group-anagrams/description/
"""


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity: nlogn * len(strs)
        if len(strs) == 0:
            return [[""]]

        map_strs = defaultdict(list)
        res = list()
        for s in strs:
            map_strs["".join(sorted(s))].append(s)
        # print(map_strs)
        for k, v in map_strs.items():
            res.append(v)
        # print(res)
        return res

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # Another Solution, time complexity: m*n [m = len(strs); n = len(s)]
        res = list()
        hash_map = dict()
        for s in strs:
            temp = [0] * 26
            for i in s:
                temp[ord(i) - 97] += 1
            # key = str(''.join(map(str, temp)))
            try:
                hash_map[tuple(temp)].append(s)
            except KeyError:
                hash_map[tuple(temp)] = list()
                hash_map[tuple(temp)].append(s)
        return hash_map.values()
