"""
Link: https://www.hackerrank.com/challenges/python-lists/problem

Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""


def list_operations():
    N = int(input())
    arr = []
    for i in range(N):
        stmt = input()
        input_r = stmt.split() if len(stmt) > 0 else [stmt]
        cmd = input_r[0]
        args = input_r[1:]
        if cmd != "print":
            eval("arr." + cmd + "(" + ",".join(args) + ")")
        else:
            print(arr)
    pass
