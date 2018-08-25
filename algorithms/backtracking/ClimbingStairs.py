"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


def climbing_stairs(n):
    # no of ways to get n steps = n-1 steps + n-2 steps
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return n

    prev, curr, next1 = 1, 2, 0
    for i in range(3, n + 1):
        next1 = curr + prev
        prev = curr
        curr = next1
    return curr
