#1.Matching {x} Repetitions
'''
S must be of length equal to 45.
The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
The last 5 characters should consist of odd digits or whitespace characters
'''
Regex_Pattern = r'^[A-Za-z02468]{40}[13579\s]{5}$'

#2.Matching {x,y} Repetitions
'''
S should begin with  or  digits.
After that, S should have 3 or more letters (both lowercase and uppercase).
Then S should end with up to 3 . symbol(s). You can end with 0 to 3 . symbol(s), inclusively.
'''
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'

#3.Matching Zero or More Repetitions
'''
S should begin with 2 or more digits.
After that, S should have 0 or more lowercase letters.
S should end with 0 or more uppercase letters
'''
Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'

#4.Matching One or More Repetitions
'''
S should begin with  or more digits.
After that, S should have 1 or more uppercase letters.
S should end with 1 or more lowercase letters.
'''
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'

#5.Matching Ending Items
'''
S should consist of only lowercase and uppercase letters (no numbers or symbols).
S should end in s.
'''
Regex_Pattern = r'^[a-zA-Z]*s$'
