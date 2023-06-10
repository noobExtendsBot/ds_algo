"""
Problem Link: https://leetcode.com/problems/3sum/description/
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        t = 0
        res = list()
        # pdb.set_trace()
        for i, v in enumerate(nums):
            # this is to skip something like
            # [-1, -1, 0, 1]
            # when there are same elements in the beginning
            if i > 0 and v == nums[i - 1]:
                continue

            l, r = i + 1, (len(nums) - 1)
            rem = t - v
            while l < r:
                c_sum = nums[l] + nums[r]
                if c_sum > rem:
                    r -= 1
                elif c_sum < rem:
                    l += 1
                elif c_sum == rem:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # [-2,0,0,2,2]
                    # This helps when there can be multiple solutions after finding one
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
