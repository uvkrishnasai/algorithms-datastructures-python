"""
Link: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""


def sherlockAndAnagrams(s):
    result = 0
    di = {}
    sub_strings = [s[i:j] for i in range(0, len(s)) for j in range(len(s), i, -1)]
    for s1 in sub_strings:
        n = len(s1)
        if n not in di:
            di[n] = []
        di[n].append(''.join(sorted(s1)))

    di2 = {}
    for value in di.values():
        print(value)
        for word in value:
            if word not in di2:
                di2[word] = [1, 0]
            else:
                k = di2[word][0]
                k += 1
                di2[word][0] = k
                di2[word][1] = k * (k - 1) // 2

    for i, j in di2.values():
        result += j
    return result
