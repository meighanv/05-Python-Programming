import re
import requests
import argparse
import bs4
from bs4 import BeautifulSoup as bs

def main(tag,url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    for t in tag:
        tags = soup.find_all(t)
        if len(tags) > 0:
            print(f'\'{t}\' tags:')
            getText(tags)
            print()
        else: 
            print(f'The website \'{url}\' does not contain any \'{t}\' tags.')

def getText(tags):
    for i in tags:
        for j in i.contents:
            if isinstance(j, bs4.element.NavigableString):
                # print(type(j))
                # print(dir(j))
                if len(j) > 1:
                    print(j)


if __name__ == '__main__': 
    # This series of statements allows for in-line arguments
    parser = argparse.ArgumentParser (description='TCP Socket Client Example') 
    parser.add_argument('--url', action="store", dest="url", type=str, required=True) 
    # This was testing how to add additional, optional arguments
    parser.add_argument('--tag', action="store", dest="tag", required=True, nargs='+')
    given_args = parser.parse_args()  
    url = given_args.url 
    tag = given_args.tag
    

main(tag,url)