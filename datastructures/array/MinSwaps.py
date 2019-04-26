"""
Link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?
h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


def minimum_swaps(arr):
    temp = [0 for i in range(len(arr))]
    count = 0
    for i in range(len(arr)):
        while temp[i] == 0:
            if i+1 == arr[i]:
                temp[i] = arr[i]
                break
            else:
                j = arr[i]-1
                arr[j], arr[i] = arr[i], arr[j]
                count += 1
    return count
