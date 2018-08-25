"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


def max_profit(prices):

    n = len(prices)
    if n == 0 or n == 1:
        return 0

    sml, big = float("Inf"), float("-Inf")
    prev = prices[0]
    maxp = 0

    for i in range(1, n):
        curr = prices[i]

        if incline(prev, curr):
            sml = prev if prev < sml else sml
            big = curr
        elif curr < sml:
            sml, big = curr, 0

        maxp = big - sml if big - sml > maxp else maxp
        # print(i, "prev: ", prev, "curr: ", curr)
        # print(i, "big: ", big, "sml: ", sml)
        prev = curr
    return maxp


def incline(prev, curr):
    return prev <= curr



