def minimumBribes(q):
    n = len(q)
    result = 0
    for i in range(1, n+1):
        if q[i-1] >= i:
            if q[i-1]-i > 2:
                print('Too chaotic')
                return
            else:
                result += q[i-1]-i
        elif i-q[i-1] > 3:
            result += 1
    print(result)
