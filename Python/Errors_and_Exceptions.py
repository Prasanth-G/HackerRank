######1.Exceptions
'''
Sample Input
3
1 0
2 $
3 1
Sample Output
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''
for i in range(int(input())):
    try:
        a, b = map(int, input().strip("\r").split(" "))
        print(a//b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)

######2.Incorrect Regex
'''
Sample Input
2
.*\+
.*+
Sample Output
True
False
'''
import re
for i in range(int(input())):
    try:
        re.compile(input())
        print('True')
    except:
        print('False')