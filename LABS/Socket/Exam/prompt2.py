""" Scraping Numbers from HTML using python modules. In this assignment you
will write a Python program similar to 
http://www.py4e.com/code3/urllink2.py. The program will read the HTML
from the data files below, and parse the data, extracting numbers and
compute the sum of the numbers in the file. """

""" We provide two files for this assignment. One is a sample file where 
we give you the sum for your testing and the other is the actual data 
you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)

Actual data: http://py4e-data.dr-chuck.net/comments_57125.html 
(Sum ends with 54)

You do not need to save these files to your folder since your program will 
read the data directly from the URL. """

import requests
import bs4
from bs4 import BeautifulSoup as bs

def main():
    # Prompt user for url
    url = input('Please provide a URL with a table:\n')

    # Grab webpage data
    r = requests.get(url)
    # Create the soup (parsed html)
    soup = bs(r.content, 'html.parser')

    # Extract all the comments with the number data
    comments = soup.find_all('span',{"class": "comments"})
    # Print a statement reflecting the URL input
    print(f'The total of the \'comments\' column in the table at \'{url}\' is:')
    # Call the commentTotal function to do the math
    print(f'{commentTotal(comments)}') 

def commentTotal(comments):
    # Init acculmulator to 0
    total = 0
    # Loop through the list 
    for comment in comments:
        # Check if the content is numeric 
        if comment.text.isnumeric() :
            # If it is, add it to the accumulator
            total += int(comment.text)
    return total

# Call main()
main()