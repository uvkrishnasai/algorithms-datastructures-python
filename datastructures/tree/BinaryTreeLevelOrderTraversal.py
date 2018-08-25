"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def level_order(self, root):

        if not root:
            return []

        arr, level = [], 0
        q = collections.deque([(root, level)])
        while q:
            node, level = q.popleft()
            if level > len(arr) - 1:
                arr.append([])

            arr[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        return arr
