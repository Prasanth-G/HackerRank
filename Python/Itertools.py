######itertools.product()
'''
Sample Input
 1 2
 3 4
Sample Output
 (1, 3) (1, 4) (2, 3) (2, 4)
 '''
from itertools import product
for each in list(product(map(int,input().split(" ")),map(int,input().split(" ")))):
    print(each,end = " ")

######itertools.permutations()
'''
Sample Input
HACK 2
Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''
from itertools import permutations
w = input().split(" ")
a = sorted(["".join(each) for each in permutations(w[0],int(w[1]))])
for each in a:
    print(each)

######itertools.combinations()
'''
Sample Input
HACK 2
Sample Output
A
C
H
K
AC
AH
AK
CH
CK
HK
'''
from itertools import combinations
w = input().split(" ")
out = ["".join(each) for i in range(1,int(w[1])+1) for each in combinations(sorted(w[0]),i)]
for each in sorted(sorted(out),key=len):
    print(each)

######itertools.combinations_with_replacement
'''
Sample Input
HACK 2
Sample Output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
from itertools import combinations_with_replacement
w = input().split(" ")
for each in sorted(["".join(each) for each in combinations_with_replacement(sorted(w[0]),int(w[1]))]):
    print(each)

######compress the string
'''
Sample Input
1222311
Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
'''
from itertools import groupby
for i,j in groupby(input()):
	print("(%d, %d) "%(len(list(j)),int(i)),end="")

######iterables and iterators
'''
Sample Input
4 
a a c d
2
Sample Output
0.8333
Explanation
All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)
Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.
Hence, the answer is 5/6.
from itertools import combinations
'''
n = int(input())
w = input().split(" ")
c = int(input())
temp = list(combinations(w, c))
print(len(["0" for i in temp if 'a' in i])/len(temp))

######Maximize it
'''
Sample Input
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output
206
Explanation
Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to (5^2 + 9^2 + 10^2)%1000 = 206
'''
import itertools
m = list(map(int, input().split(" ")))
out = 0
inp = []
for i in range(m[0]):
    inp.append(list(map(int, input().split(" ")))[1:])
g = 0
for each in itertools.product(*inp):
    temp = sum([x**2 for x in each])%m[1]
    if g < temp:
        g = temp
print(g)