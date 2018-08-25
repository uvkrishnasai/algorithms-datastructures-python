"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""


def compare_version(version1, version2):
    ver1 = version1.split('.')
    ver2 = version2.split('.')
    n = max(len(ver1), len(ver2))
    while len(ver1) <= n:
        ver1.append('0')
    while len(ver2) <= n:
        ver2.append('0')
    for i in range(0, n):
        if int(ver1[i]) == int(ver2[i]):
            continue
        return 1 if int(ver1[i]) > int(ver2[i]) else -1
    return 0
