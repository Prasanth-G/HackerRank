#1.Matching specific string
Regex_Pattern = r'hackerrank'

#2.Matching Anything But a Newline
regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"

#3.Matching Digits & Non-Digit Characters
Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"

#4.Matching Whitespace & Non-Whitespace Character
Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"

#5.Matching Word & Non-word Character
Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"

#6.Matching Start & End
Regex_Pattern = r"^\d\w{4}\.$"