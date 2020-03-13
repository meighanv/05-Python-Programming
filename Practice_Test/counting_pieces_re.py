import re

"""
# Write a function count_pieces that counts the number of digits, non-digit characters (excluding white spaces),
# whitespace characters and words in a string. The function takes a string as input and returns
# a list of integers that represents the counts.
For example, "We have 8 digits.", the output list will be [1, 13, 3, 4],
1: digits (ONLY 8)
13: non-digit characters (excluding white spaces)
3: white spaces
4: words

"""


def count_pieces(testString):
    whitespace = re.compile(r'\s')
    nonDigit = re.compile(r'[^\d\s:]')
    digits = re.compile(r'\d')
    words = re.compile(r'[A-Za-z0-9]+')
    
    outputList = [len(digits.findall(testString)),
               len(nonDigit.findall(testString)), 
               len(whitespace.findall(testString)), 
               len(words.findall(testString))]

    return outputList

#print(count_pieces("1 2 3 4"))




