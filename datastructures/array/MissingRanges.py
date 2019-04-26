"""
Given a sorted integer array nums,
where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""


def find_missing_ranges(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """
    if len(nums) == 0:
        return ["{}->{}".format(lower, upper)] if upper-lower > 0 else ["{}".format(lower)]

    res = []
    for i in range(0, len(nums)):
        prev = lower if i == 0 else lower + 1

        if prev < nums[i]:
            diff = nums[i]-prev
            if diff > 1:
                res.append("{}->{}".format(prev, nums[i ]-1))
            else:
                res.append("{}".format(nums[i ]-1))

        lower = nums[i]

        if i == len(nums)-1 and nums[i] < upper:
            if upper-nums[i] > 1:
                res.append("{}->{}".format(nums[i]+1, upper))
            else:
                res.append("{}".format(nums[i]+1))

    return res
