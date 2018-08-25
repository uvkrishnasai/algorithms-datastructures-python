"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""


def reverse_words(str):
    if len(str) == 0:
        return

    temp = "".join(str)
    words = temp.split()
    rev_words = words[::-1]
    result = " ".join(rev_words)
    for i in range(0, len(result)):
        str[i] = result[i]

    pass
