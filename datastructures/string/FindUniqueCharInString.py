"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


def first_uniq_char(s):
    a = [-1 for i in range(26)]
    for i in s:
        b = ord(i)-ord('a')
        a[b] += 1
    for i in range(0, len(s)):
        b = ord(s[i])-ord('a')
        if a[b] == 0:
            return i
    return -1
