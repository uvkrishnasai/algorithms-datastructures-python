"""
Link: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

Given two strings, a and b, that may or may not be of the same length,
determine the minimum number of character deletions required to make a and b anagrams.
Any characters can be deleted from either of the strings.

For example, if a=cde and b=dcf,
we can delete e from string a and f from string b so that both remaining strings are cd and dc which are anagrams.

"""


def make_anagram(a, b):
    ltr_counts = [0 for i in range(26)]

    for char in a:
        ltr_counts[ord(char) - ord('a')] += 1

    for char in b:
        ltr_counts[ord(char) - ord('a')] -= 1

    return sum([abs(i) for i in ltr_counts])