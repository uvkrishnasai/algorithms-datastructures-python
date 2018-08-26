"""
Maximize It
Link: https://www.hackerrank.com/challenges/maximize-it/problem
"""
from itertools import product


def compute_max(elem, m, max):
    new_max = (sum([(i ** 2) for i in elem])) % m
    return new_max if new_max > max else max


if __name__ == '__main__':
    k, m = tuple(input().split())
    # print("{}, {}".format(k, m))
    arr = [[int(i) for i in input().split()[1:]] for i in range(int(k))]
    max = 0
    for i in product(*arr):
        max = compute_max(i, int(m), max)
    print(max)
