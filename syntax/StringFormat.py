"""
You are given the firstname and lastname of a person on two different lines.
Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Input Format
The first line contains the first name, and the second line contains the last name.

Sample Input 0
Ross
Taylor

Sample Output 0
Hello Ross Taylor! You just delved into python.
"""


def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))
    pass


"""
In Python, a string of text can be aligned left, right and center.

.ljust(width)
This method returns a left aligned string of length width.
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  

.center(width)
This method returns a centered string of length width.
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----

.rjust(width)
This method returns a right aligned string of length width.
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank

Task
You are given a partial code that is used for generating the HackerRank Logo of variable thickness. 
Your task is to replace the blank (______) with rjust, ljust or center.

Output Format

Output the desired logo.

Sample Input

5
Sample Output

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
"""


def format():
    # Replace all ______ with rjust, ljust or center.

    thickness = int(input())  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print(c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)

    # Top Pillars
    for i in range(thickness + 1):
        print(c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)

    # Middle Belt
    for i in range((thickness + 1) / 2):
        print(c * thickness * 5).center(thickness * 6)

        # Bottom Pillars
    for i in range(thickness + 1):
        print(c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)

        # Bottom Cone
    for i in range(thickness):
        print((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6)
    pass


"""
Text Wrap:

Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""


def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])


"""
Designer door mat:

Sample Input
9 27

Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""


def designer_door_mat():
    specs = input().split()
    arr = [('.|.'*(2*i+1)).center(int(specs[1]), '-') for i in range(0, int(specs[0])//2)]
    print('\n'.join(arr))
    print('WELCOME'.center(int(specs[1]), '-'))
    print('\n'.join(arr[::-1]))
