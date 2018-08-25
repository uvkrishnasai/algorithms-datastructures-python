"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closest_value(self, root, target):
        closest_node = self.closest_helper(root, target)
        return closest_node.val

    def closest_helper(self, node, target):

        closest = node
        if node.left is not None and target <= node.val:
            # search left subtree
            print("search left subtree:", node.left.val)
            closest = self.closest_helper(node.left, target)

        if node.right is not None and target >= node.val:
            # search right subtree
            print("search right subtree:", node.right.val)
            closest = self.closest_helper(node.right, target)

        # is between left and parent
        if node.left is not None and node.left.val <= target and target <= node.val:
            print("is between left and parent:", node.left.val, node.val)
            new_closest = node if target - node.left.val > node.val - target else node.left
            closest = self.get_closest(closest, new_closest, target)

        # is between parent and right
        if node.right is not None and node.right.val >= target and target >= node.val:
            print("is between parent and right:", node.val, node.right.val)
            new_closest = node if target - node.val < node.right.val - target else node.right
            closest = self.get_closest(closest, new_closest, target)

        return closest

    def get_closest(self, first, second, target):
        return first if (abs(target - first.val) < abs(target - second.val)) else second
