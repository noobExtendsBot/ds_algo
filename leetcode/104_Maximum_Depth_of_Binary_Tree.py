"""
Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxHeight(self, c_node):
        l_height = r_height = 0

        if c_node is None:
            return 0
        if c_node.left is not None:
            l_height = self.maxHeight(c_node.left)
        if c_node.right is not None:
            r_height = self.maxHeight(c_node.right)
        return max(l_height, r_height) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.maxHeight(root)
        return depth
