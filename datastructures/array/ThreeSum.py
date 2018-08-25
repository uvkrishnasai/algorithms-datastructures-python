def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    result = []
    result_2 = set([])
    n = len(nums)
    r = sorted(nums)
    for i in range(0, n):
        if r[i] > 0:
            break
        for j in range(i + 1, n):
            temp = (-1 * (r[i] + r[j]))
            temp2 = r[j + 1:]
            if temp in temp2:
                temp3 = [r[i], r[j], temp]
                if tuple(temp3) not in result_2:
                    result_2.add(tuple(temp3))
                    result.append(temp3)

    return result
