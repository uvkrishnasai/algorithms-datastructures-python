def find_repeat(the_list):
    a = 0
    one_set = False
    for elem in the_list:
        temp = 1 << (elem-1)
        #print(bin(a), bin(temp), bin(1 << (elem-1)))
        if elem == 1:
            if one_set:
                return 1
            one_set = True

        if a & temp:
            return elem
        a |= temp
    return 0


actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
print(actual)