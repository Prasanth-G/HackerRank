#1.Positive Lookahead
'''
Write a regex that can match all occurrences of o followed immediately by oo in S.
'''
Regex_Pattern = r'o(?=oo)'

#2.Negative Lookahead
'''
Write a regex which can match all characters which are not immediately followed by that same character.
'''
Regex_Pattern = r"(.)(?!\1)"

#3.Positive Lookbehind
'''
Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.
'''
Regex_Pattern = r"(?<=[13579])\d"

#4.Negative Lookbehind
'''
Write a regex which can match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).
'''
Regex_Pattern = r"(?<![aeiouAEIOU])."
