"""
In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings.
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""


def split_and_join(line):
    return "-".join(line.split())


"""
Merge the tools:
Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
"""


def merge_the_tools(string, k):
    print("\n".join(
        ["".join(sorted(set(e), key=e.index)) for e in
         [string[i:i+k] for i in range(0, len(string),k)]
        ]
    ))
