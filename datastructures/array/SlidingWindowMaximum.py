"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""


def max_sliding_window(nums, k):
    if len(nums) == 0 or k > len(nums):
        return []

    if k == 0:
        return max(nums)

    if k == 1:
        return nums

    maxi = [max(nums[:k])]
    for i in range(k, len(nums), 1):
        if nums[i] > maxi[:-2:-1][0]:
            maxi += [nums[i]]
            continue
        maxi += maxi[:-2:-1]
    return maxi
