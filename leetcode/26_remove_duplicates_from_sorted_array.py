"""
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        prev = 0
        nxt = prev + 1
        while prev < nxt and nxt < (len(nums)):
            if nums[nxt] == nums[prev]:
                nums[prev] = None
            prev += 1
            nxt += 1
        nums[:] = [x for x in nums if x is not None]
        return len(nums)
