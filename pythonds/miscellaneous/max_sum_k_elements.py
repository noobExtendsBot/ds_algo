"""
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum possible for ‘k’ consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700
"""
import pdb

def max_sum(nums, k):
    mx_sum = 0
    for i in range(0,k):
        mx_sum += nums[i]

    c_sum = mx_sum
    # pdb.set_trace()
    for i in range(k, len(nums)):
        c_sum -= nums[i-k]
        c_sum += nums[i]
        mx_sum = max(c_sum, mx_sum)

    return mx_sum

    

if __name__=="__main__":
    print(max_sum([100, 200, 300, 400], k=2))
    print(max_sum([100, 200, 100, 400, 500, 2, 600], k=5))