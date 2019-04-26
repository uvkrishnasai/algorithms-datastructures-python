def fib(n):
    assert n >= 0

    if n == 0 or n == 1:
        return n

    prev, curr = 0, 1
    for i in range(2, n+1, 1):
        prev, curr = curr, prev+curr
    return curr


actual = fib(0)
expected = 0
assert(actual == expected)

actual = fib(1)
expected = 1
assert(actual == expected)

actual = fib(2)
expected = 1
print(actual)
assert(actual == expected)

actual = fib(3)
expected = 2
print(actual)
assert(actual == expected)

actual = fib(5)
expected = 5
assert(actual == expected)

actual = fib(10)
expected = 55
assert(actual == expected)

try:
    fib(-1)
except AssertionError:
    print("Assertion Error!")