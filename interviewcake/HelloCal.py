meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]

n = len(meetings)
assert(meetings)
if n == 1:
    print(meetings)
meetings.sort(key = lambda x: x[0])

i = 1
while i < n:
    prev = meetings[i-1]
    curr = meetings[i]
    print(meetings, i, n, prev)
    if prev[0] <= curr[0] <= prev[1]:
        start = prev[0]
        end = prev[1] if prev[1] >= curr[1] else curr[1]
        meetings[i-1] = (start, end)
        del meetings[i]
        n -= 1
    else:
        prev = curr
        i += 1

print(meetings)
