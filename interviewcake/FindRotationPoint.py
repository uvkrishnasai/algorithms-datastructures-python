def find_rotation_point(words):

    low, mid, high = 0, 0, len(words)-1

    while high-low > 0:
        mid = low+((high-low)//2)
        if words[low] > words[mid]:
            high = mid
        elif words[mid] > words[high]:
            low = mid
        else:
            break

        if high-low == 1:
            return mid+1

    return mid


out = find_rotation_point(['grape', 'orange', 'plum', 'radish', 'apple'])
assert(out == 4)

out = find_rotation_point(['cape', 'cake'])
assert(out == 1)

out = find_rotation_point(['cake', 'cape'])
assert(out == 0)

out = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                           'undulate', 'xenoepist', 'asymptote',
                           'babka', 'banoffee', 'engender',
                           'karpatka', 'othellolagkage'])
assert(out == 5)