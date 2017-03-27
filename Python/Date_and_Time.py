######1.Calendar Module
'''
Sample Input
08 05 2015
Sample Output
WEDNESDAY
'''
from datetime import datetime
print(datetime.strptime(input(),'%m %d %Y').strftime('%A').upper())

######2.Time Delta
'''
Sample Input
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 +0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 +0000
Sample Output
25200           #absolute difference in seconds
88200
'''
import datetime
for i in range(int(input())):
    d = datetime.datetime.strptime(input(),"%a %d %b %Y %X %z") - datetime.datetime.strptime(input(),"%a %d %b %Y %X %z")
    print(abs(int(d.total_seconds())))