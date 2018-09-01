######1.Introduction to Sets
'''
Sample Input :
10
161 182 161 154 176 170 167 171 170 174
Sample Output :
169.375
Explanation :
Here, set([154, 161, 167, 170, 171, 174, 176, 182]) is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.
'''
def average(array):
    a = set(array)
    return sum(a)/len(a)

######2.No Idea!
'''
Sample Input :
3 2
1 5 3
3 1
5 7
Sample Output :
1
Explanation :
You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.
Hence, the total happiness is 2 - 1 = 1.
'''
input()
arr = [ int(each) for each in input().split(" ")]
A = set([int(each) for each in input().split(" ")])
B = set([int(each) for each in input().split(" ")])
happiness = 0
for each in arr:
    if each in A:
        happiness = happiness + 1
    elif each in B:
        happiness = happiness - 1
print(happiness)

######3.Symmetric Difference
'''
Sample Input :
4
2 4 5 9
4
2 4 11 12
Sample Output :
5
9
11
12
'''
input()
a = input().split(" ")
input()
b = input().split(" ")
a = set(a)
b = set(b)
output = sorted([ int(each) for each in a.difference(b).union(b.difference(a)) ])
for each in output:
    print(each)

######4. Set.add()
'''
Sample Input :
7
UK
China
USA
France
New Zealand
UK
France 
Sample Output :
5
Explanation :
UK and France repeat twice. Hence, the total number of distinct country stamps is 5 (five).
'''
print(len(set([input() for i in range(int(input()))])))

######5. Set .discard(), .remove() & .pop()
'''
Sample Input :
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output :
4
Explanation :
After completing these 10 operations on the set([4]), we get set. Hence, the sum is 4.
'''
n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    temp = input().split(" ")
    if temp[0] == "pop":
        s.pop()
    elif temp[0] == "remove" or temp[0] == "discard":
        s.discard(int(temp[1]))
print(sum(s))

######6. Set .union() Operation
'''
Sample Input :
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output :
13
Explanation :
Roll numbers of students who have at least one subscription:
1,2,3,4,5,6,7,8,9,10,11,21 and 55. Roll numbers: 1, 2, 3, 6 and 8 are in both sets so they are only counted once.
Hence, the total is 13 students.
'''
input()
a = set(map(int,input().split(" ")))
input()
b = set(map(int,input().split(" ")))
print(len(list(a.union(b))))

######7. Set .intersection() Operation
'''
Sample Input :
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output :
5
Explanation :
The roll numbers of students who have both subscriptions:
1,2,3,6 and 8.
Hence, the total is 5 students.
'''
input()
a = set(map(int,input().split(" ")))
input()
b = set(map(int,input().split(" ")))
print(len(list(a.intersection(b))))

######8. Set .difference() Operation
'''
Sample Input :
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output :
4
Explanation :
The roll numbers of students who only have English newspaper subscriptions are:
4, 5, 7 and 9.
Hence, the total is 4 students.
'''
input()
a = set(map(int,input().split(" ")))
input()
b = set(map(int,input().split(" ")))
print(len(list(a.difference(b))))

######9. Set .symmetric_difference() Operation
'''
Sample Input :
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output :
8
'''
input()
a = set(map(int,input().split(" ")))
input()
b = set(map(int,input().split(" ")))
print(len(list(a.symmetric_difference(b))))

######10. Set Mutations
'''
Sample Input :
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Sample Output :
38
'''
input()
s = set(map(int, input().split(" ")))
for each in range(int(input())):
    temp = input().split(" ")
    if temp[0] == "intersection_update":
        s.intersection_update(set(map(int, input().split(" "))))
    elif temp[0] == "update":
        s.update(set(map(int, input().split(" "))))
    elif temp[0] == "symmetric_difference_update":
        s.symmetric_difference_update(set(map(int, input().split(" "))))
    elif temp[0] == "difference_update":
        s.difference_update(set(map(int, input().split(" "))))
print(sum(s))

######11. The Captain's Room
'''
Sample Input :
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Sample Output :
8
'''
n = int(input())
d = {}
for each in input().split(" "):
    if each in d:
        d[each] = d[each] + 1
    else:
        d[each] = 1
for each in d:
    if d[each] == 1:
        print(each)
        break

######12. Check Subset
'''
Sample Input :
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output :
True 
False
False
Explanation :
Set A = {1 2 3 5 6} 
Set B = {9 8 5 6 3 2 1 4 7} 
All the elements of set A are elements of set B. 
Hence, set A is a subset of set B.
'''
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print(A.issubset(B))

######13. Check Strict Superset
'''
Sample Input :
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output :
False
Explanation :
Set A is the strict superset of the set ([1,2,3,4,5]) but not of the set ([100, 11, 12]) because 100 is not in set A. 
Hence, the output is False.
'''
A = set(input().split())
is_ss = lambda x : x.issubset(A) and bool(A.difference(x))
print(all([ is_ss(set(input().split())) for i in range(int(input())) ]))