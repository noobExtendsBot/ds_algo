"""
Problem Link: https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_arr  = [1 for i in range(len(nums))]
        backward_arr = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                forward_arr[i] = 1
            else:
                forward_arr[i] = forward_arr[i-1]*nums[i-1]
        j = len(nums)-1
        while j >= 0:
            if j == len(nums) - 1:
                backward_arr[j] = 1
            else:
                backward_arr[j] = backward_arr[j+1]*nums[j+1]
            j -= 1

        nums[:] = [forward_arr[i]*backward_arr[i] for i in range(len(nums))]
        return nums
        