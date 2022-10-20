"""
Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
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

    def inorder(self, c_node):
        # <left> <root> <right>
        if c_node is None:
            return
        
        self.inorder(c_node.left)
        self.res.append(c_node.val)
        self.inorder(c_node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.inorder(root)
        return self.res