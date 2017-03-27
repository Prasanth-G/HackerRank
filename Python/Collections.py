######1.collection.Counter()
'''
Sample Input
10                      #no.of shoes
2 3 4 5 6 8 7 6 5 18    #shoes size
6                       #no.of customers
6 55                    #customer's size, price
6 45
6 55
4 40
18 60
10 50
Sample Output
200
'''
from collections import Counter
input()
size = Counter(map(int, input().split(" ")))
amt = 0
for each in range(int(input())):
    i = list(map(int,input().split(" ")))
    if i[0] in size:
        size[i[0]] = size[i[0]] - 1
        if not size[i[0]]:
            size.pop(i[0])
        amt = amt + i[1]
print(amt)

######2.DefaultDict Tutorial
'''
Output M lines. 
The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.
Sample Input
5 2         #M, N
a           #M words
a
b
a
b
a           #N testcase
b
Sample Output
1 2 4
3 5
'''
from collections import defaultdict
d = defaultdict(list)
m, n = input().split(" ")
count = 1
for i in range(int(m)):
    d[input()].append(count)
    count = count + 1
for i in range(int(n)):
    inp = input()
    if inp in d:
        for each in d[inp]:
            print(each,end=" ")
        print("")
    else:
        print(-1)

######3.Coolections.namedtuple()
'''

Sample Input
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6 
Sample Output
78.00       #average mark
'''
from re import findall
n = int(input())
index = findall("(\S+)\s",input()).index("MARKS")
print(sum([int(findall("(\S+)\s",input())[index]) for i in range(n)])/n)

######4.collections.OrderedDict()
'''
Sample Input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output
BANANA FRIES 12     #item_name, total price in order
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''
from collections import OrderedDict
import re
output = OrderedDict()
for i in range(int(input())):
    item = re.findall("(.+) (\d+)",input())[0]
    if item[0] in output:
        output[item[0]] = output[item[0]] + int(item[1])
    else:
        output[item[0]] = int(item[1])
for each in output:
    print(each,output[each])

######5.Word Order
'''
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
3               #no.of occurrence in input order
2 1 1
'''
from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
    word = input()
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
print(len(d))
for each in d:
    print(d[each],end = " ")

######6.Collections.deque() #de = double ended
'''
Sample Input
6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output
1 2
'''
from collections import deque
d = deque()
for i in range(int(input())):
    w = input().split(" ")
    w[0] = w[0].strip("\r")
    if w[0] == "append":
        d.append(w[1].rstrip("\r"))
    elif w[0] == "pop":
        d.pop()
    elif w[0] == "appendleft":
        d.appendleft(w[1].rstrip("\r"))
    elif w[0] == "popleft":
        d.popleft()
for each in d:
    print(each,end=" ")

######7.Piling up!
'''
Sample Input
2
6
4 3 2 1 3 4
3
1 3 2
Sample Output
Yes
No
'''
from collections import deque
import sys
for i in range(int(input())):
    input()
    i = input().split(" ")
    temp = [ int(each) for each in i if each.strip("\n") ]
    sidelengths = deque(temp)
    prevlength = sys.maxsize
    output = "Yes"
    while len(sidelengths):
        if len(sidelengths) == 1 or sidelengths[0] < sidelengths[-1]:
            currlength = sidelengths.pop()
        else:
            currlength = sidelengths.popleft()
        if currlength > prevlength:
            output = "No"
            break
        prevlength = currlength
    print(output)

######8.Most common
'''
Sample Input
aabbbccde
Sample Output
b 3
a 2
c 2
'''
from collections import Counter
c = Counter(input())
s = sorted(c)
def val(each):
    return c[each]
for each in sorted(s, key= val, reverse= True)[:3]:
    print(each,c[each])