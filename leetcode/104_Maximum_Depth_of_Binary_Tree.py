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
    def maxNodes(self, c_node):
        if c_node is None:
            return 0
        l_height = self.maxNodes(c_node.left)
        r_height = self.maxNodes(c_node.right)
        return max(l_height, r_height) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.maxNodes(root)
        return depth
