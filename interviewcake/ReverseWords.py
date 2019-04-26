def reverse_chars(chars, i, j):
    print(i, j)
    n = len(chars)
    k = 0
    for i in range(i, i+((j-i)//2)):
        chars[i], chars[j-k-1] = chars[j-k-1], chars[i]
        k += 1
    pass


message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']

n = len(message)
if n == 0 or n == 1:
    print([])

reverse_chars(message, 0, n)
print(message)

i = 0
for j in range(0, n+1, 1):
    #print(i, j, message[j])
    if j == n or message[j] == ' ':
        if i == j:
            continue
        reverse_chars(message, i, j)
        i = j+1

print(message)

