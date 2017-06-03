#1.Matching Same text again & again
'''
must be of length: 20 
1st character: lowercase letter .
2nd character: word character .
3rd character: whitespace character .
4th character: non word character .
5th character: digit .
6th character: non digit .
7th character: uppercase letter .
8th character: letter (either lowercase or uppercase).
9th character: vowel (a, e, i , o , u, A, E, I, O or U).
10th character: non whitespace character .
11th character: should be same  as 1st character .
12th character: should be same  as 2nd character .
13th character: should be same  as 3rd character .
14th character: should be same  as 4th character .
15th character: should be same  as 5th character .
16th character: should be same  as 6th character .
17th character: should be same  as 7th character .
18th character: should be same  as 8th character .
19th character: should be same  as 9th character .
20th character: should be same  as 10th character .
'''
Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([AEOIUaeiou])(\S)\1\2\3\4\5\6\7\8\9\10'

#2.Backreferences to Failed groups
'''
S consists of 8 digits.
S may have "-" separator such that string S gets divided in 4 parts, with each part having exactly two digits. (Eg. 12-34-56-78)
'''
Regex_Pattern = r"^\d\d(-?)\d\d(\1)\d\d(\2)\d\d$"

#3.Branch reset Groups - Perl
'''
S consists of 8 digits.
S must have "---", "-", "." or ":" separator such that string S gets divided in 4 parts, with each part having exactly two digits.
S string must have exactly one kind of separator.
Separators must have integers on both sides.
'''
$Regex_Pattern = '^[0-9]{2}(?|(---)|(:)|(\.)|(-))[0-9]{2}\1[0-9]{2}\1[0-9]{2}$';

#4.Forward References - Perl
'''
S consists of tic or tac.
tic should not be immediate neighbour of itself.
The first tic must occur only when tac has appeared at least twice before.
'''
$Regex_Pattern = '^(tactactic)(tactic)*(tac)*$';
