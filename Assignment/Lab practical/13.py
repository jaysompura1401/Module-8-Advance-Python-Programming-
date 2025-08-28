#Q13. Write a Python program to match a word in a string using re.match(). 

import re

# Input string
text = "Python is a powerful programming language."

# Word to match
pattern = r"Python"

# Using re.match() (matches only at the beginning of the string)
match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")
