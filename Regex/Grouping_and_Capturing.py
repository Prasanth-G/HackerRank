#1.Matching Word Boundaries
'''
You have a test String S. 
Your task is to write a regex which will match word starting with vowel (a,e,i,o, u, A, E, I , O or U). 
The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only. 
The matched word must start and end with a word boundary.
'''
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

#2.Capturing & Non-Capturing Groups
'''
You have a test String S.
Your task is to write a regex which will match S with the following condition:
S should have 3 or more consecutive repetitions of ok.
'''
Regex_Pattern = r'okokok'

#3.Alternative Matching
'''
Given a test string, S, write a RegEx that matches S under the following conditions:
S must start with Mr., Mrs., Ms., Dr. or Er..
The rest of the string must contain one or more English alphabetic letters (upper and lowercase).
'''
Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)([A-Za-z]+)$'