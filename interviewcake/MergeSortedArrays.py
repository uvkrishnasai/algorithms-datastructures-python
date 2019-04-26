
def solve():
    my_list = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]

    if not my_list:
        print(alices_list)

    if not alices_list:
        print(my_list)

    res = []
    n, m = len(my_list), len(alices_list)
    i, j = 0, 0

    while i < n and j < m:
        my_elem, alices_elem = my_list[i], alices_list[j]
        print(my_elem, alices_elem)
        if my_elem < alices_elem:
            res.append(my_elem)
            i += 1
            continue
        if alices_elem < my_elem:
            res.append(alices_elem)
            j += 1
            continue
        if my_elem == alices_elem:
            res.append(my_elem)
            res.append(alices_elem)
            i += 1
            j += 1

    if i < n:
        res.extend(my_list[i:])

    if j < m:
        res.extend(alices_list[j:])

    print(res)

solve()
