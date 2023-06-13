import pdb

from collections import deque



def maxArea(height):
    if len(height) == 2: return height[0]*height[1]

    mx = 0
    first = 0
    next = 1

    while next < len(height) and first < len(height):
        l = max(next, first) - min(next, first)
        h = min(height[first], height[next])
        A = l*h
        if A > mx: mx = A
        if height[first] < height[next]: first += 1
        else: next += 1
    
    return mx

        

if __name__=="__main__":
    print(maxArea([1, 5, 4, 3]))
    print(maxArea([3, 1, 2, 4, 5]))
    print(maxArea([5,5,5,5,5,5]))