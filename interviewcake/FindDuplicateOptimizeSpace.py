def find_repeat(the_list):
    assert the_list
    n = len(the_list)
    assert (n > 1)
    l, r = 1, n - 1
    cnt = 0
    while l < r:
        cnt += 1
        mid = ((r - l) // 2) + l
        m = mid
        sum_ = 0
        for i in the_list:
            if l < i <= m:
                sum_ += 1

        sublist_leng = m - l + 1
        print(the_list, l, m, r, sum_, sublist_leng)
        if sum_ < sublist_leng:
            r = mid
        else:
            l = mid

        if r - l == 1:
            break

        print(the_list, l, m, r, sum_, sublist_leng)
    return l


actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
print(actual)
actual = find_repeat([1, 2, 5, 5, 5, 5])
print(actual)
actual = find_repeat([1, 2, 3, 2])
print(actual)
actual = find_repeat([1, 1])
print(actual)
