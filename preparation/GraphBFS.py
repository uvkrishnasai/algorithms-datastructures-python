"""
input = [
    (1, 3), (3, 2), (2, 4), (4, 5), (8, 5), (5, 9),
    (3, 6), (10, 6), (6, 4), (4, 7), (7, 9)
]

in_1, in_2 = [], []
for elem in input:
    in_1.append(elem[0])
    in_2.append(elem[1])

out_1 = set(in_1) - set(in_2)
in_4 = Counter(in_2)
out_2 = []

for k, v in in_4.items():
    if v == 1:
        out_2.append(k)

print(in_4)
print(out_1)
print(out_2)
"""

nums = [2, 7, 11, 15]
k = 9
mape = {v: i for i, v in enumerate(nums)}
for i, v in enumerate(nums):
    if k-v in mape:
        print([i, mape[k-v]])
        break

