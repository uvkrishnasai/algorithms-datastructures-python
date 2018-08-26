"""
Given the names and grades for each student in a Physics class of  students, s
tore them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.

Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0
Berry
Harry

Link: https://www.hackerrank.com/challenges/nested-list/problem
"""


if __name__ == '__main__':
    students = [[input(), float(input())] for _ in range(int(input()))]
    students = sorted(students, key=lambda x: (x[1], x[0]))
    min_grade = students[0][1]
    second_min = None
    i = 1
    while i < len(students):
        if second_min is not None and students[i][1] > second_min:
            # break the loop as the grade is greater than 2nd min
            break
        elif second_min is not None and students[i][1] == second_min:
            # print student as grade == 2ndmin
            print(students[i][0])
        elif students[i][1] > min_grade:
            # get the second min score and print the student
            second_min = students[i][1]
            print(students[i][0])
        i += 1
    pass
