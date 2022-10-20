"""
Problem Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
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

    def postOrder(self, c_node):
        if c_node is None:
            return

        self.postOrder(c_node.left)
        self.postOrder(c_node.right)
        self.res.append(c_node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postOrder(root)
        return self.res
