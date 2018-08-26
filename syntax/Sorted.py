"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5
"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score_sheet = sorted(arr, key=lambda x: -x)
    max = score_sheet[0]
    for elem in score_sheet:
        if elem < max:
            print(elem)
            break
    pass


"""
Athlete Sort:
Link: https://www.hackerrank.com/challenges/python-sort-sort/problem
"""


def athlete_sort():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr = sorted(arr, key=lambda x: x[k])
    for elem in arr:
        print(*elem)
    pass


"""
You are given a string S. 
S contains alphanumeric characters only. 
Your task is to sort the string S in the following manner:
ginortS

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format
A single line of input contains the string S.

Sample Input
Sorting1234

Sample Output
ginortS1324
"""


def conditional_sorting():
    print(
        *sorted(
            list(input()),
            key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2 == 0, x.isupper(), x)
        ),
        sep=""
    )
    pass
