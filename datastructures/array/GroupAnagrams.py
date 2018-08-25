"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    if len(strs) == 0:
        return []

    result_map = {}
    for str in strs:
        sume = ''.join(sorted(list(str)))
        if sume not in result_map:
            result_map[sume] = []
        result_map[sume].append(str)
    return list(result_map.values())
