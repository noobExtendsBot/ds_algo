"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have multiple solutions, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sums(nums, target):
    hash_map = dict()
    indicies = list()
    for i, v in enumerate(nums):
        rem = target - v
        if rem in hash_map:
            indicies.append([i, hash_map[rem]])
        else:
            hash_map[v] = i
    return indicies


if __name__ == "__main__":
    nums = [0, 5, 4, -6, 2, 7, 13, 3, 1]
    target = 4
    print(two_sums(nums, target))
