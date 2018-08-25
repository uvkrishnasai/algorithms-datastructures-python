"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def build_tree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        pstart = [0]
        cache = {v: k for k, v in enumerate(inorder)}
        return self.helper(cache, preorder, inorder, pstart, 0, len(inorder) - 1)

    def helper(self, cache, preorder, inorder, pstart, istart, iend):

        if istart > iend:
            return

        root_val = preorder[pstart[0]]
        root = TreeNode(root_val)
        pstart[0] = pstart[0] + 1

        if istart == iend:
            return root

        iind = cache[root_val]

        root.left = self.helper(cache, preorder, inorder, pstart, istart, iind - 1)
        root.right = self.helper(cache, preorder, inorder, pstart, iind + 1, iend)

        return root
