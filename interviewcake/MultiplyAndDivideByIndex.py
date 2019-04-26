in_list = [1, 7, 3, 4]
n = len(in_list)
prod = 1
res1 = []
for i, elem in enumerate(in_list):
    prod *= elem
    res1.append(prod)

prod = 1
res2 = []
for i in range(n-1, -1, -1):
    prod *= in_list[i]
    res2.insert(0, prod)

left = 1
right = 1
res = []
for i in range(n):
    if i != 0:
        left = res1[i-1]

    if i != n-1:
        right = res2[i+1]

    res.append(left*right)

print(res)
