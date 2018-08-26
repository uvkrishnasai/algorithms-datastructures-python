"""
SubSet:

You are given two sets, A and B.
Your job is to find whether set  is a subset of set .

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
"""


def sub_set():
    n = int(input())
    for i in range(n):
        a_len = input()
        a = [int(i) for i in input().split()]
        b_len = input()
        b = [int(i) for i in input().split()]

        result = True
        for x in a:
            if x not in b:
                result = False
                break
        print(result)

"""
Strict SubSet:

You are given a set A and n other sets. 
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example 
Set([1,3,4]) is a strict superset of set([1,3]). 
Set([1,3,4]) is not a strict superset of set([1,3,4]). 
Set([1,3,4]) is not a strict superset of set([1,3,5]).

Input Format

The first line contains the space separated elements of set A. 
The second line contains integer n, the number of other sets. 
The next n lines contains the space separated elements of the other sets.

Sample Input 0
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0
False
"""

def strict_sub_set():
    a = [int(i) for i in input().split()]
    print(
        all(set(a).issuperset(set([int(i) for i in input().split()])) for _ in range(int(input())))
    )
