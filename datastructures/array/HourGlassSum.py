"""
https://www.hackerrank.com/challenges/2d-array/problem
?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Ans = 7


-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

 Ans: 28
"""


def hourglass_sum(arr):
    if len(arr) == 0:
        return 0

    m = len(arr[0])
    n = len(arr)

    matrix = [[0 for i in range(m - 2)] for j in range(n - 2)]

    for i in range(0, m - 2):
        for j in range(0, n - 2):
            matrix[i][j] = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                j + 1] + arr[i + 2][j + 2]

    return max([max(mat) for mat in matrix])
