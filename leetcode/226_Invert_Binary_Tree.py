"""
Problem Link: https://leetcode.com/problems/invert-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderToInvert(self, c_node):
        if c_node is None:
            return None

        self.postorderToInvert(c_node.left)
        self.postorderToInvert(c_node.right)
        # l, r = c_node.left, c_node.right
        c_node.left, c_node.right = c_node.right, c_node.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        self.postorderToInvert(root)
        return root
