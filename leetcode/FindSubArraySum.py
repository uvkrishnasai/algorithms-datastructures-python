from collections import defaultdict


def findSubarraySum(arr, n, Sum):

    prevSum = defaultdict(lambda: 0)
    res = 0
    currsum = 0

    for i in range(0, n):

        currsum += arr[i]

        if currsum == Sum:
            res += 1

        print(currsum, Sum, prevSum)
        if (currsum - Sum) in prevSum:
            res += prevSum[currsum - Sum]

        prevSum[currsum] += 1

    return res


if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    Sum = -10
    n = len(arr)
    print(findSubarraySum(arr, n, Sum))
