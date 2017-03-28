######1.Map and Lambda Function
'''
Sample Input
5
Sample Output
[0, 1, 1, 8, 27]
'''
cube = lambda x: x**3# complete the lambda function 
def fibonacci(n):
    x = -1
    y = 1
    fseries = []
    temp = 0
    for i in range(n):
        temp = x + y
        fseries.append(temp)
        x,y = y, temp
    return fseries

######2.Validating Email Addresses with a Filter
'''
Sample Input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
Sample Output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''
import re
def fun(s):
    return bool(re.match("[\w-]+@[A-Za-z0-9]+\.\w{0,3}$",s))# return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

######3.Reduce Function
'''
Sample Input
3
1 2
3 4
10 6
Sample Output
5 8
Explanation
Required product is (1/2)*(3/4)*(10/6) = (5/8)
'''
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = Fraction(reduce(lambda x,y: x*y,fracs))
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

