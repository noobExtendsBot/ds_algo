"""
Problem Link: https://leetcode.com/problems/validate-binary-search-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sorted = list()

    def inorder_traversal(self, c_node):
        if c_node is None:
            return
        self.inorder_traversal(c_node.left)
        self.sorted.append(c_node.val)
        self.inorder_traversal(c_node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder_traversal(root)
        flag = True
        for i in range(len(self.sorted) - 1):
            if self.sorted[i] >= self.sorted[i + 1]:
                flag = False
                break
        return flag
