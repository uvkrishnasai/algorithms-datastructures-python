def summaryRanges(nums):
    ranges, r = [], []
    for n in nums:
        if n-1 not in r:
            r = []
            ranges += r,
        r[1:] = n,
        print(ranges)
        print(r)
    return ['->'.join(map(str, r)) for r in ranges]


print(summaryRanges([0, 1, 2, 4, 5, 7]))