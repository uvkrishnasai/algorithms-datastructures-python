"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root):
        left_arr = []
        right_arr = []

        self.recurive_left(root, left_arr)
        self.recurive_right(root, right_arr)

        # print(" ".join([str(i.val) for i in left_arr]))
        # print(" ".join([str(i.val) for i in right_arr]))
        return (left_arr == right_arr)

    def recurive_left(self, node, arr):

        if node is None:
            return

        if node.left is None:
            arr.append(float("Inf"))
        else:
            arr.append(node.left.val)

        if node.right is None:
            arr.append(float("Inf"))
        else:
            arr.append(node.right.val)

        if node.left is not None:
            self.recurive_left(node.left, arr)

        if node.right is not None:
            self.recurive_left(node.right, arr)

        pass

    def recurive_right(self, node, arr):

        if node is None:
            return

        if node.right is None:
            arr.append(float("Inf"))
        else:
            arr.append(node.right.val)

        if node.left is None:
            arr.append(float("Inf"))
        else:
            arr.append(node.left.val)

        if node.right is not None:
            self.recurive_right(node.right, arr)

        if node.left is not None:
            self.recurive_right(node.left, arr)
        pass
