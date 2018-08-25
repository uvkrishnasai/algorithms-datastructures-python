"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""


def max_sub_array_len(arr, k):
    sum, max = 0, 0
    value_map = {}
    for i in range(0, len(arr)):
        sum += arr[i]

        if sum == k:
            max = i + 1

        if sum not in value_map:
            value_map[sum] = i

        # print("value_map: ", value_map)
        # print("max: ", max, "sum-k", sum-k, "i: ", i)
        # print("----------------------")
        if sum - k in value_map:
            if max < (i - value_map[sum - k]):
                max = i - value_map[sum - k]

    # print("----------------------")
    return max
