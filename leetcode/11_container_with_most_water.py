"""
Problem Link: https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return 1 * min(height[0], height[1])

        mx = 0
        first = 0
        last = len(height) - 1

        while first < len(height) and last > first:
            l = max(last, first) - min(last, first)
            h = min(height[first], height[last])
            A = l * h
            if A > mx:
                mx = A
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1

        return mx
