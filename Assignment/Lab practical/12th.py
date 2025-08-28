# Q12. Write a Python program to search for a word in a string using re.search().

import re

# Input string
text = "Python is a powerful programming language."

# Word to search
word = "powerful"

# Using re.search() to find the word
match = re.search(word, text)

if match:
    print(f" Word '{word}' found at position {match.start()} to {match.end()}.")
else:
    print(f" Word '{word}' not found in the text.")
