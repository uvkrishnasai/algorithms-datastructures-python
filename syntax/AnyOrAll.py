"""
any()
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.

Code
>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False

all()
This expression returns True if all of the elements of the iterable are true.
If the iterable is empty, it will return True.

Code
>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False

Task
You are given a space separated list of integers.
If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format
The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N integers.

Sample Input
5
12 9 61 5 14

Sample Output
True
"""

if __name__ == '__main__':
    n, arr = input(), input().split()
    print(all([int(i) > 0 for i in arr]) and any([x == x[::-1] for x in arr]))