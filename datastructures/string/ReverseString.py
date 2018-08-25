"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"

"""


def reverse_string(s):
    return ''.join([s[i] for i in range(len(s) - 1, -1, -1)])
