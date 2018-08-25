"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def longest_palindrome(s):
    n = len(s)

    if n == 0 or n == 1:
        return s

    matrix = [[False for i in range(n)] for j in range(n)]

    # len == 1
    max = 1
    palindrome = s[0]
    for i in range(0, n):
        matrix[i][i] = True

    # len == 2
    for i in range(0, n - 1):
        if s[i] == s[i + 1]:
            matrix[i][i + 1] = True
            palindrome = s[i:i + 1 + 1] if max == 1 else palindrome
            max == 2

    # len > 2
    k = 3
    while k <= n:
        i, j = 0, k - 1
        while j < n:
            if s[i] == s[j] and matrix[i + 1][j - 1]:
                matrix[i][j] = True
                palindrome = s[i:j + 1] if max < k else palindrome
                max = k
            i += 1
            j += 1
        k += 1

    return palindrome
