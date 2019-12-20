# Write a Python program somewhat similar to 
# http://www.py4e.com/code3/json2.py. The program
#  will prompt for a URL, read the JSON data from 
# that URL using urllib and then parse and extract 
# the comment counts from the JSON data, compute the 
# sum of the numbers in the file and enter the sum below:
# Here are two files for this assignment. One is a sample
#  file where we give you the sum for your testing and the 
# other is the actual data you need to process for the 
# assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)

# Actual data: http://py4e-data.dr-chuck.net/comments_57128.json (Sum ends with 10)

import urllib.request as request
import json

def main():
    # Prompt user for url
    url = input('Please provide a json URL with the counts:\n')

    # grab page with json data
    page = request.urlopen(url)

    # Read the body of the page (expected to contain json data)
    body = page.read()
    
    # decode json data
    j = json.loads(body.decode("utf-8"))
    sumCount(j)
    # Statements used to examine objects during dev
    #print(j['comments'])
    #print(type(j))

def sumCount(j):
    total = 0
    try:
        for i in j['comments']:
            try:
                total += i['count']
            except KeyError:
                print('Program expects a nested key of \'count\' which does not exist.')
    except KeyError:
        print('Program expects a key of \'comments\' which does not exist') 
    print(f'Sum of counts in the provided json file: {total}')
    return total

main()