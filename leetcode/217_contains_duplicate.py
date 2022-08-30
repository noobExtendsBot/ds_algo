"""
Problem Link: https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map_nums = dict()
        for i in nums:
            if map_nums.get(i) is None:
                map_nums[i] = 1
            else:
                return True
        return False
