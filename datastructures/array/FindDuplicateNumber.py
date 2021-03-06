"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

Bit Manipulations:
==================
Set a bit
bit_fld |= (1 << n)
Clear a bit
bit_fld &= ~(1 << n)
Toggle a bit
bit_fld ^= (1 << n)
Test a bit
bit_fld & (1 << n)
"""


def find_duplicate(nums):
    n = len(nums)
    if n == 0:
        return ""

    a = 0
    for i in nums:
        n = 1 << i
        m = a & n
        if m != 0:
            return i
        a = a | 1 << i
    pass
