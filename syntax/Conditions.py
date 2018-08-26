def is_weird(n):
    if n > 0:
        if n%2 == 0:
            if n >= 6 and n <= 20:
                print("Weird")
                return
        else:
            print("Weird")
            return
    print("Not Weird")
    return


if __name__ == '__main__':
    N = int(input())
    is_weird(N)
