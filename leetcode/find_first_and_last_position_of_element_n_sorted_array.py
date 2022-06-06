"""
Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
            nums = [5,7,7,8,8,10], target = 8 => [3,4]
            if empty [-1,-1]
            if only one [5,7,7,8,10], target = 8 => [3,3]

            METHOD 1: linear search
            METHOD 2: Binary Search
        """

        # Brute force (a bad question maybe? accepts it)
        # time complexity O(n)
        """ Brute FOrce start """
        # res = [-1, -1]
        # for index, value in enumerate(nums):
        #     if value == target:
        #         # if our res[0] is -1 list empty then first match also make res[1] (if only one element)
        #         # else update the last position
        #         if res[0] == -1:
        #             res[0] = index
        #             res[1] = index
        #         else:
        #             res[1] = index
        # return res
        """ Brute Force end """
        """ Binary Search Method start """
        # time complexity log(n)
        res = [-1, -1]
        # first get the first location (left bound)
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                res[0] = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
                
        start, end = 0, len(nums)-1
        # get the last location (right bound)
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                res[1] = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        
        return res
        """ Binary Search Method end """