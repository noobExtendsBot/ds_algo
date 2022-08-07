"""
Problem Link: https://leetcode.com/problems/rotate-array/
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k == l:
            return nums
        else:
            k %= l
            nums[:] = nums[l - k:] + nums[:l - k]
