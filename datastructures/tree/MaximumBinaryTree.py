"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def construct_maximum_binary_tree(self, nums):
        return self.build_tree(nums)

    def build_tree(self, nums):
        if nums is None or len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        maxi = max(nums)
        ind = nums.index(maxi)
        node = TreeNode(maxi)
        leftNode = self.build_tree(nums[:ind])
        rightNode = self.build_tree(nums[ind + 1:])
        node.left = leftNode
        node.right = rightNode

        return node
