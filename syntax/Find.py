"""
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Sample Input
ABCDCDC
CDC

Sample Output
2

Concept

There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where s is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])

A range function is used to loop over some length:
range (0, 5)
Here, the range loops over 0 to 4. 5 is excluded.
"""


def count_substring(string, sub_string):
    return len(
        [
            1
            for elem in [
            string[i:i + len(sub_string)] for i in range(0, len(string) - len(sub_string) + 1)
        ]
            if sub_string == elem
        ])
