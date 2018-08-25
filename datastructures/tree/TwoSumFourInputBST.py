"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""


import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find_target(self, root, k):
        arr, q = set([]), collections.deque([])
        q.append(root)
        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

            diff = k - node.val
            if diff in arr:
                return True

            arr.add(node.val)

        return False
