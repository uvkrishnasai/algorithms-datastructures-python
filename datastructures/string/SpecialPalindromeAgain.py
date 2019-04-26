"""
Link: https://www.hackerrank.com/challenges/special-palindrome-again/problem
?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
"""


def substr_count(n, s):
    result = 0
    k = 2
    while k <= n:
        result += sum([1 if is_valid(s[i: i+k], k) else 0 for i in range(0, n-k+1)])
        k += 1
    return result + n


def is_valid(s, k):
    m = k // 2
    left, right = s[:m], s[m:] if k % 2 == 0 else s[m + 1:]
    return left == right and len(set(left)) == 1