string = """
1. Recognize the following strings: “bat,” “bit,” “but,” “hat,”
“hit,” or “hut.”
​
2. Match any pair of words separated by a single space, that is,
first and last names.
​
3. Match any word and single letter separated by a comma and
single space, as in last name, first initial.
​
4. Match the set of all valid Python identifiers.
​
5. Match a street address according to your local format (keep
your regex general enough to match any number of street
words, including the type designation). For example, American
street addresses use the format: 1180 Bordeaux Drive. Make
your regex flexible enough to support multi-word street
names such as: 3120 De la Cruz Boulevard.
​
6. Match simple Web domain names that begin with “www.”
and end with a “.com” suffix; for example, www.yahoo.com.
Extra Credit: If your regex also supports other high-level
domain names, such as .edu, .net, etc. (for example,
www.foothill.edu).
​
7. Match the set of all valid e-mail addresses (start with a loose
regex, and then try to tighten it as much as you can, yet
maintain correct functionality). Try to break what we did in class 
and improve it.
​
8. Match the set of all valid Web site addresses (URLs) (start
with a loose regex, and then try to tighten it as much as you
can, yet maintain correct functionality).Try to break what we did in 
class and improve it.
​
9. type(). The type() built-in function returns a type object,
which is displayed as the following Pythonic-looking string:
​
    # >>> type(0)
    # <type 'int'>
    # >>> type(.34)
    # <type 'float'>
    # >>> type(dir)
<type 'builtin_function_or_method'>
​
Create a regex that would extract the actual type name from
the string. Your function should take a string like this <type
'int'> and return int. (Ditto for all other types, such as
‘float’, ‘builtin_function_or_method’, etc.) Note: You
are implementing the value that is stored in the __name__
attribute for classes and some built-in types.
​
10. Processing Dates. In Section 1.2, we gave you the regex pattern
that matched the single or double-digit string representations of
the months January to September (0?[1-9]). Create the regex
that represents the remaining three months in the standard
calendar.
​
Meighan, V
​
"""

# Ex. 1******************************************
import re
# pattern = re.compile(r'[HB].t', re.IGNORECASE)
# matches = pattern.findall(string)

# print(type(matches))
# for match in matches:
#     print(match)

# Ex. 2******************************************
# pattern = re.compile(r'[A-Z]\w+\s{1}[A-Z]\w+')
# matches = pattern.findall(string)

# print(type(matches))
# for match in matches:
#     print(match)

# Ex. 3******************************************
# pattern = re.compile(r'[A-Z]\w+,\s{1}[A-Z]\.?\s')
# matches = pattern.findall(string)

# print(type(matches))
# for match in matches:
#     print(match)

# Ex. 4******************************************

# import keyword as kw
# ids = """
# gfg
# 123
# _abc12
# #abc
# class


# """

# pattern = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
# matches = pattern.findall(ids)

# for match in matches:
#     if kw.iskeyword(match) == False:
#         print(f'{match}: Valid Identifier')

# Ex. 5 ******************************************
# pattern = re.compile(r'\d+\s[A-Za-z]*\s{1}[A-Za-z]*\s?\w*\s?\w*')
# matches = pattern.findall(string)

# for match in matches:
#     print(f'{match}')

# Ex. 6 ******************************************
pattern = re.compile(r'(w{3}\.)?([a-zA-Z0-9]*)(\.[a-zA-Z]{2,3})')
matches = pattern.findall(string)

for match in matches:
    print(f'{match}')