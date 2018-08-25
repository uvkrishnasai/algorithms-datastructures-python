"""
Given two non-empty binary trees s and t,
check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_subtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_arr = []
        t_arr = []

        if not s or not t:
            return False

        self.dfs(s, s_arr)
        self.dfs(t, t_arr)

        return "".join(t_arr) in "".join(s_arr)

    # pre order traversal
    def dfs(self, node, arr):
        arr.append("-{}-".format(str(node.val)))

        if node.left:
            self.dfs(node.left, arr)
        else:
            arr.append("-{}-".format("x"))

        if node.right:
            self.dfs(node.right, arr)
        else:
            arr.append("-{}-".format("x"))
