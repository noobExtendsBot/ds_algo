"""
Problem link: https://leetcode.com/problems/longest-consecutive-sequence/description/
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        mx = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            l = 0
            if (nums[i]-1) not in nums_set:
                c_start = nums[i]
                while c_start in nums_set:
                    c_start += 1
                    l += 1
            if l > mx:
                mx = l
        return mx
             
        