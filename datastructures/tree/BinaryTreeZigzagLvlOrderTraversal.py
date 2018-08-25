"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between)

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzag_level_order(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        q = collections.deque([])
        dic = collections.OrderedDict()
        q.append((1, root))
        while q:
            lvl, node = q.popleft()
            if lvl not in dic:
                dic[lvl] = []

            dic[lvl].append(node.val)

            l, r = (node.left, node.right)

            if l:
                q.append((lvl + 1, l))

            if r:
                q.append((lvl + 1, r))

        res = list(dic.values())
        return [res[i][::-1] if i % 2 == 1 else res[i] for i in range(0, len(res))]
