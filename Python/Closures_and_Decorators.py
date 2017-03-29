# A decorator is just a callable that takes a function as an argument
#and returns a replacement function. 
#
#
######1.Standardize Mobile number using Decorators
'''
Sample Input
3
07895462130
919875641230
9195969878
Sample Output
+91 78954 62130
+91 91959 69878
+91 98756 41230
'''
def wrapper(f):
    def fun(l):
        l = ['+91 '+phone_no[-10:-5]+' '+phone_no[-5:] for phone_no in l]
        return f(l)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

######2.Decorators 2 - Name Directory
'''
Sample Input
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Sample Output
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
'''
import operator
def person_lister(f):
    def inner(people):
        #people = sorted(people, key= operator.itemgetter(2))
        #return f(people)
        return map(f, sorted(people, key=operator.itemgetter(2)))
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
