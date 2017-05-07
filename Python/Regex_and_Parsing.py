######1.Introduction to Regex Module
'''
Sample input :
5
1.414
+.5486468
0.5.0
1+1.0
0
Sample output :
True
True
False
False
False
'''
import re
for i in range(int(input())):
    print(bool(re.match("^[\+\-]?\d*\.\d+$",input())))

######2.re.split()
'''
Sample input :
.172..16.52.207,172.16.52.117
Sample Output :
172
16
52
207
172
16
52
117     #print only the numbers
'''
import re
[ print(i) for i in re.split("[.,]",input()) if i]

######3.Group(), Groups() & Groupdict() 
'''
Sample Input :
..12345678910111213141516171820212223
Sample Output :
1
Explanation
.. is the first repeating character, but it is not alphanumeric. 
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
'''
import re
out = re.findall(r'([A-Za-z0-9])\1',input())
if out:
    print(out[0])
else:
    print(-1)

######4.Re.findall() & Re.finditer() 
'''
Sample Input :
rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output :
ee
Ioo
Oeo
eeeee
Explanation :
ee is located between d consonant f and . 
Ioo is located between k consonant m and . 
Oeo is located between p consonant r and . 
eeeee is located between t consonant t and .
'''
import re
pattern = re.compile(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]*([AEIOUaeiou]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]')
match = pattern.findall(input())
match = [each for each in match if len(each) >= 2]
if match:
    print(*match, sep='\n')
else:
    print("-1")

######5.Re.start() & Re.end()
'''
Sample Input :
aaadaa
aa
Sample Output :
(0, 1)  
(1, 2)
(4, 5)
'''
import re
s, k = input(), input()
l = list(re.finditer('(?=('+ k +'))',s))
if l:
    for each in l:
        print((each.start(),each.end()+len(k)-1))
else:
    print((-1,-1))
######6.Regex Substitution
'''
Sample Input :
11
a = 1;
b = input();
if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Sample Output :
a = 1;
b = input();
if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
'''
import re
import functools
for i in range(int(input())):
    print(functools.reduce(lambda x,z: re.sub(z[0],z[1],x),[(r'(?<=\s)\|\|(?=\s)','or'), (r'(?<=\s)&&(?=\s)','and')], input()))

######7.Validating Roman Numerals
'''
Sample Input :
CDXXI
Sample Output :
True
'''
import re
print(bool(re.fullmatch(r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})',input())))

######8.Validating Phone numbers
'''
Sample Input :
2
9587456281
1252478965
Sample Output :
YES
NO
'''
import re
for i in range(int(input())):
    if re.fullmatch(r'[987][0-9]{9}',input()):
        print("YES")
    else:
        print("NO")

######9.Validating and Parsing email addresses
'''
Sample Input :
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
Sample Output :
DEXTER <dexter@hotmail.com>
Explanation :
A valid email address meets the following criteria:
    => It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
    => The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
    => The domain and extension contain only English alphabetical characters.
    => The extension is 1,2,3 or  characters in length.
'''
import email.utils
import re
for i in range(int(input())):
    name, addr = email.utils.parseaddr(input())
    if re.fullmatch(r'[a-zA-Z][\w\-\.]*@[a-zA-Z]+?\.[a-zA-Z]{0,3}', addr):
        print(email.utils.formataddr((name, addr)))

######10.Hex colour code
'''
Sample Input :
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
Sample Output :
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
'''
import re
for i in range(int(input())):
    line = input()
    if len(line) and line[0] != '#':
        output = re.findall('#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}',line)
        if output:
            print(*output,sep='\n')

######11.HTML parser - part 1
'''
Sample Input :
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
Sample Output :
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
'''
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        self.print_(attrs)
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        self.print_(attrs)
    def print_(self,attrs):
        for each in attrs:
            print("-> %s > %s"%each)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())

######12.HTML parser - part 2
'''
Sample Input :
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
Sample Output :
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        l = comment.split('\n')
        if len(l) > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(*l, sep='\n')
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data\n%s"%data)
            
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

######13.Detect HTML Tags, Attributes and Attribute Value
'''
Sample Input :
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
Sample Output :
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
'''
from html.parser import HTMLParser

class myhtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_(attrs)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.print_(attrs)
    def print_(self, attrs):
        for each in attrs:
            print("-> %s > %s"%each)

html = ''            
for i in range(int(input())):
    html = html + input() + '\n'
htmlparser = myhtmlparser()
htmlparser.feed(html)
htmlparser.close()

######14.Validating UID
'''
Sample Input :
2
B1CD102354
B1CDEF2354
Sample Output :
Invalid
Valid
'''
import re
print(*[ 'Valid ' if not re.search(r'([A-Z0-9a-z]).*\1', text) and re.search(r'[A-Z].*[A-Z]', text) and re.search(r'\d.*\d.*\d', text) and len(text) == 10 else 'Invalid' for text in [input() for i in range(int(input()))]], sep='\n')

######15.Validating Credit Card Numbers
'''
Sample Input :
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
Sample Output :
Valid
Valid
Invalid
Valid
Invalid
Invalid
Explanation :
A valid credit card from ABCD Bank has the following characteristics: 
► It must start with a 4,5 or 6. 
► It must contain exactly 16 digits.
► It must only consist of digits (0-9). 
► It may have digits in groups of 4 , separated by one hyphen "-". 
► It must NOT use any other separator like ' ' , '_', etc. 
► It must NOT have 4 or more consecutive repeated digits.
'''
import re
print(*['Valid' if re.search(r'^[4-6][0-9]{3}\-{0,1}[0-9]{4}\-{0,1}[0-9]{4}\-{0,1}[0-9]{4}$',text) and not re.findall(r'([0-9])\1\1\1',''.join(text.split('-'))) else 'Invalid' for text in [input() for i in range(int(input()))]], sep='\n')

######16.Validating Postal Codes
'''
Sample Input :
110000
Sample Output :
False
Explanation :
A postal code P must be a number in the range of (100000, 999999).
A postal code P must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
'''
import re
code = input()
print(len(code) == 6 and code.isdigit() and len(re.findall(r'(?=([0-9])\d\1)', code)) <= 1)

######17.Matrix Script
'''
Sample Input :
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
Sample Output :
This is Matrix#  %!
'''
import re
def func(string):
    string = string.group(0)
    return ' '.join([string[0], string[-1]])

m, n = map(int, input().split())
l = [input() for i in range(m)]
decoded_str = ''.join([ ''.join([each[i] for each in l]) for i in range(n)])
print(re.sub(r'\w[!@#$%& ]+\w', func, decoded_str))
