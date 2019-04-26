from collections import Counter


def solve(the_string):
    counter = Counter(the_string)
    return sum(0 if i % 2 == 0 else 1 for i in counter.values()) in {0, 1}


print(solve("ivicc"))
print(solve("aabccbdd"))
print(solve(""))
print(solve("aabcd"))
