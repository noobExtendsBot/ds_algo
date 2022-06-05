"""
Problem Link: https://leetcode.com/problems/binary-search/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init variables
        start, end = 0, len(nums) - 1
        # loop until list has been parsed
        while start <= end:
            # get lower bound for mid
            mid = (start + end) // 2
            if nums[mid] == target:
                # if element is found return position
                return mid
            elif nums[mid] > target:
                # if target element smaller than mid element then reduce the
                # list size from the end
                end = mid - 1
            else:
                # if target element greater than mid element then reduce the
                # list size from the start
                start = mid + 1
        return -1
