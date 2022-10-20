"""
Problem Link: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.res = list()

    def preOrder(self, c_node):
        if c_node is None:
            return

        self.res.append(c_node.val)
        self.preOrder(c_node.left)
        self.preOrder(c_node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        self.preOrder(root)
        return self.res
