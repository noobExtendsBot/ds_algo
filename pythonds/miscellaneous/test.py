import pdb

from collections import deque


def three_sum(nums):
    nums = sorted(nums)
    t = 0
    res = list()
    # pdb.set_trace()
    for i, v in enumerate(nums):
        # pdb.set_trace()
        if i > 0 and v == nums[i-1]:
            continue

        l, r = i+1, (len(nums) - 1)
        rem = t - v
        while l < r:
            c_sum = nums[l] + nums[r]
            if c_sum > rem:
                r -= 1
            elif c_sum < rem:
                l += 1
            elif c_sum == rem:
                # pdb.set_trace()
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # what's the point of this?????
                while nums[l] == nums[l-1] and l<r:
                    # print(nums[l], nums[l-1])
                    l += 1

    return res
        

if __name__=="__main__":
    print(three_sum([0,0,0]))