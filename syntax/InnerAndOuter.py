from numpy import inner
from numpy import outer


def numpy_inner(a, b):
    print(inner(a,b))


def numpy_outer(a, b):
    print(outer(a,b))


if __name__ == '__main__':
    a = input()
    b = input()
    a1 = [int(i) for i in a.split()]
    b1 = [int(i) for i in b.split()]
    numpy_inner(a1, b1)
    numpy_outer(a1, b1)