"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_valid_bst(self, root):

        if root is None or root.val is None:
            return True

        arr = []
        self.inorder_traverse(root, arr)

        for i in range(1, len(arr)):
            if (arr[i] <= arr[i - 1]):
                return False

        return True

    def inorder_traverse(self, node, arr):
        if node.left:
            self.inorder_traverse(node.left, arr)

        arr.append(node.val)

        if node.right:
            self.inorder_traverse(node.right, arr)
        pass
