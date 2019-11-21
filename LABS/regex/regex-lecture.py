# Regular Expressions

import re

text_to_match = """lol lolololol
Daniel abcd 1234 abcd 
this-thing@gmail.com\t
this.other_thing@gmail.com
lol lolololol
210-444-4444
512*888*8888
800-444-4444
900-555-5555

Mr. Anderson
Mr Smith
Ms. Davis
Mrs. Robinson
Mr. T

cat,bat,pat,mat"""

# 'r' before a string indicates raw string literal which ignores escape chars
#print(r'\tTab')

# match()
# determines if the regex matches at the BEGINNING of the string
# Returns 'None' if its not at BEGINNING, same as ^anchor


# my_string = 'tkinter is the best GUI library out there'

# Compile allows us to separate our pattern matches into a variable
# pattern = re.compile(r'Daniel')
# match = pattern.match(text_to_match)
# Result is <re.Match object; span=(0, 6), match='Daniel'>
# span is useful to slice the string 
# print(match)
# that makes it easier to reuse our variable 
# my_match = re.compile(r'Tkinter')


# Search() let's us search the entire string
# Best to use over match unless you know it has to be at start of
# string 
# pattern = re.compile(r'1234')
# searched_item = pattern.search(text_to_match)
# print(searched_item)


# finditer()
# finds all instances of literal string and stores as
#  callable iterator 

# pattern = re.compile(r'abcd')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)
# # **********************META CHARS************************
# # '.' will match any non-newline character
# pattern = re.compile(r'.')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # find literal '.' in string
# pattern = re.compile(r'\.')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # find digits in string
# pattern = re.compile(r'\d')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # find non-digits in string
# pattern = re.compile(r'\D')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # find non-digits in string
# # includes new lines, special characters, just no numbers 
# pattern = re.compile(r'\D')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Find any word char (a-z, A-Z, 0-9, _)
# pattern = re.compile(r'\w')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Find any non-word char (a-z, A-Z, 0-9, _)
# pattern = re.compile(r'\W')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Find any whitespace 
# pattern = re.compile(r'\s')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Find any non-whitespace 
# pattern = re.compile(r'\S')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)


#*******************ANCHORS***********************
# Anchors don't match characters; they match invisible positions before
#  or after characters

# \b - finds word boundaries ( if there is a space in front of a character) 
# Find any boundary matches 
# pattern = re.compile(r'\blol')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Find any non-boundary matches 
# pattern = re.compile(r'\Blol')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # ^ - finds matches at beginning of string
# pattern = re.compile(r'^lol')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # $ - finds matches at end of string
# pattern = re.compile(r'lol$')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# finds 3 digits in a row
# pattern = re.compile(r'\d\d\d')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # find phone number
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)


# find using a character set [], used to search for a group of characters
# pattern = re.compile(r'\d\d\d[-*]\d\d\d[-*]\d\d\d\d')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# pattern = re.compile(r'[89]00[-*]\d\d\d[-*]\d\d\d\d')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Find a range of values
# # using pipe to match either set
# pattern = re.compile(r'[a-d]|[A-D]')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Find a range of values
# # Another way to get same effect as using pipe to match either set
# pattern = re.compile(r'[a-dA-D]')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Find a range of values
# # Negative char set search
# pattern = re.compile(r'[^1-7]')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # Match cat, mat, pat, but not bat
# pattern = re.compile(r'[^bB]at')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

#***********************************************************
#QUANTIFIERS

# pattern = re.compile(r'(\d{3}.){3}')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # ? - find 0 or 1 match

# pattern = re.compile(r'Mr\.?')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # + finds 1 or more
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # * - for 0 or more
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

# # () - an anchor that allows us to match several different patterns
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_match)

# print(type(matches))
# for match in matches:
#     print(match)

emails = """
TestUser@gmail.com
test.user@school.edu
test-123-user@this-place.net
"""

# # Matching for e-mails
# pattern = re.compile(r'[a-zA-z]+@[a-zA-Z]+\.com')
# matches = pattern.finditer(emails)

# print(type(matches))
# for match in matches:
#     print(match)

# # Matching for e-mails
# pattern = re.compile(r'[a-zA-z.0-9-_+]+@[a-zA-Z.0-9-_]+\.[a-zA-Z0-9-.]+')
# matches = pattern.finditer(emails)

# print(type(matches))
# for match in matches:
#     print(match)

urls = """
http://testsite.com
https://www.google.com
https://youtube.com
https://www.nasa.gov
"""
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# matches = pattern.finditer(urls)

# print(type(matches))
# for match in matches:
#     print(match)


# # We can group all of these to grab groups
# # groups 0 being  all groups, 1 being first group, etc. 
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# matches = pattern.finditer(urls)

# print(type(matches))
# for match in matches:
#     print(match.group(0,1,2,3))


# Return domains
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)

# findall() - finds all and returns as tuples if there is more than one group
pattern = re.compile(r'(Mr|Ms|Mrs)\.?(\s[A-Z]\w*)')
matches = pattern.findall(text_to_match)

print(type(matches))
for match in matches:
    print(match)

# Shows findall() without groups; returns list of strings
# pattern = re.compile(r'[a-zA-z.0-9-_+]+@[a-zA-Z.0-9-_]+\.[a-zA-Z0-9-.]+')
# matches = pattern.findall(emails)

# print(type(matches))
# for match in matches:
#     print(match)

# flags

string = 'I cAan TyPeE GOod'

# case-insensitive search; re.I works for re.IGNORECASE
pattern = re.compile(r'[ao]', re.IGNORECASE)
matches = pattern.findall(string)

print(type(matches))
for match in matches:
    print(match)

