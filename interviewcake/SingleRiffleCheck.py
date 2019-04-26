def solve():
    half1 = [1, 4, 5]
    half2 = [2, 3, 6]
    shuffled_desk = [1, 2, 3, 4, 5, 6]
    i, j, k = 0, 0, 0
    m, n, o = len(half1), len(half2), len(shuffled_desk)
    if o != (m+n):
        return False
    print("lengths equal")
    while k < o-1:
        i_next_num = half1[i] if i < m else None
        j_next_num = half2[j] if j < n else None
        k_next_num = shuffled_desk[k]

        print(k_next_num, i_next_num, j_next_num)

        if k_next_num == i_next_num:
            i += 1
            k += 1
            continue

        if k_next_num == j_next_num:
            j += 1
            k += 1
            continue

        return False

    return True


print(solve())
