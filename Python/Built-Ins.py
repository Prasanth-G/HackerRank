#######1.Zipped!
'''
Sample Input
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
Sample Output
90.0 
91.0 
82.0 
90.0 
85.5      
'''
ns, n = map(int, input().split(" "))
marks = [list(map(float, input().split(" "))) for i in range(n)]
zipped = zip(*marks)
print(*[ sum(each)/n for each in list(zipped)],sep='\n')

#######2.Input()
'''
Sample Input
1 4                     #x and k
x**3 + x**2 + x + 1
Sample Output
True
'''
x, k = map(int, raw_input().split())
print(input() == k)

######3.Python Evaluation
'''
Sample input
print(2 + 3)
Sample Output
5
'''
eval(input())

######4.Sort Data
'''
Sample input
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation
The table is sorted on the second attribute shown as  K = 1 because it's 0-indexed.
'''
n, m = map(int, input().split(' '))
L = [ list(map(int,input().split(' '))) for i in range(n)]
k = int(input())
[print(("%d "*m)%tuple(each)) for each in sorted(L, key= lambda x: x[k])]

######5.All or Any
'''
Sample input
5
12 9 61 5 14
Sample Output
True
'''
input()
inp = input().split(" ")
print(all([int(x) >= 0 for x in inp]) and any([list(reversed(x)) == list(x) for x in inp]))

######6.ginortS
'''
Sample Input
Sorting1234
Sample Output
ginortS1324
Note: 
a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0. 
b) You can only use one sorted function in your code. A 0 score will be awarded for using sorted more than once. 

Hint: Success is not the key, but key is success.
'''
import functools
def val(a):
    if a.islower():
        return ord(a) - ord('a')
    elif a.isupper():
        return ord(a) - ord('A') + 26
    elif a.isdigit():
        if int(a)%2:
            return int(a) + 53
        else:
            return int(a) + 63
print(functools.reduce(lambda x,y : x + y, sorted(input(), key=val)))