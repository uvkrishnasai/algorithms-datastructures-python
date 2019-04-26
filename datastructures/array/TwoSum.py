"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum(nums, target):
    for i in range(0, len(nums) - 1, 1):
        other_elem = target - nums[i]
        index = find(nums, i, other_elem)
        if index > -1 and i != index:
            return [i, index]
    return [-1, -1]


def find(nums, i, other_elem):
    try:
        if nums[i] == other_elem:
            return nums.index(other_elem, i + 1)
    except Exception:
        return -1
    else:
        return nums.index(other_elem)
    pass
