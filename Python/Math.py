######1.Polar Coordinates
'''
Sample Input
  1+2j
Sample Output
 2.23606797749979 
 1.1071487177940904
 '''
 import cmath
a = complex(input())
print(abs(a))
print(cmath.phase(a))

######2.Find Angle MBC
'''
Sample Input
10
10
Sample Output
45°
'''
import math
ab = int(input())
bc = int(input())
print("%d°"%round(math.degrees(math.acos(bc/math.sqrt(ab**2 + bc**2)))))

######3.Triangle Quest 2
'''
Sample Input
5
Sample Output
1
121
12321
1234321
123454321
'''
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
     print((10**i - 1)** 2//81)

######4.Mod Divmod
'''
Sample Input
177
10
Sample Output
17
7
(17, 7)
'''
a,b = divmod(int(input()),int(input()))
print(a)
print(b)
print("(%d, %d)"%(a,b))

######5.Power - Mod Power
'''
Sample Input
3
4
5
Sample Output
81
1
'''
a,b = int(input()),int(input())
print(pow(a,b))
print(pow(a,b,int(input())))

######6.Integer comes in All Sizes
'''
Sample Input
9
29
7
27
Sample Output
4710194409608608369201743232  
'''
print(int(input())**int(input()) + int(input())**int(input()))

######7.Triangle Quest
'''
Sample Input
5
Sample Output
1
22
333
4444
'''
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**i-1)//9 * i)