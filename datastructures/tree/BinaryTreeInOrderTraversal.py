"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        if not root:
            return res

        self.inorder_traversal_helper(root, res)
        return res

    def inorder_traversal_helper(self, root, res):
        if root.left:
            self.inorder_traversal_helper(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorder_traversal_helper(root.right, res)
