"""
Problem Link: https://leetcode.com/problems/two-sum/
"""

from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums = defaultdict(list)
        for k, v in enumerate(nums):
            rem = target - v
            if map_nums.get(rem, None) is None:
                map_nums[v] = k
            else:
                return [map_nums.get(rem), k]

        # my first optimised solution was
        # map_nums = defaultdict(list)
        # for k,v in enumerate(nums):
        #     map_nums[v].append(k)

        # for k,v in enumerate(nums):
        #     rem = target - v
        #     if map_nums.get(rem, None) is None or map_nums.get(rem)[0] == k:
        #             continue
        #     if len(map_nums.get(rem)) == 2:
        #             return map_nums.get(rem)
        #     else:
        #         return [k, map_nums.get(rem)[0]]
