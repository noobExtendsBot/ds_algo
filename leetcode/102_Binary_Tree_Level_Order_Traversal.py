"""
Problem Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        res = list()
        queue.append(root)
        while queue:
            r_count = len(queue)
            temp = list()
            while r_count:
                c_node = queue.popleft()
                temp.append(c_node.val)
                if c_node.left:
                    queue.append(c_node.left)
                if c_node.right:
                    queue.append(c_node.right)
                r_count -= 1
            res.append(temp)
        return res
