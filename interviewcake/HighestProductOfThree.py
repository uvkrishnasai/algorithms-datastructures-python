def highest_product_of_3(list_of_ints):
    assert list_of_ints
    assert(len(list_of_ints) >= 3)

    list_of_ints.sort()

    min_prod = list_of_ints[0] * list_of_ints[1]
    max_prod = list_of_ints[-2] * list_of_ints[-3]
    maxe = list_of_ints[-1]

    return max((min_prod * maxe), (max_prod * maxe))


out = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
print(out)
