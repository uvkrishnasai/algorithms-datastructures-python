def is_leap(year):
    leap = False

    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        leap = True

    return leap


def print_function(n):
    for i in range(1, n+1):
        print(i, end="")
    pass
