import requests
import argparse

def main(url):
    try:
        r = requests.get(url)
        print(r.content)
    except requests.exceptions.ConnectionError as e:
        print(f'Error: {e.strerror}. This site ({url}) probably doesn\'t exist.')
    


if __name__ == '__main__': 
    # This series of statements allows for in-line arguments
    parser = argparse.ArgumentParser (description='TCP Socket Client Example') 
    parser.add_argument('--url', action="store", dest="url", type=str, required=True) 
    # This was testing how to add additional, optional arguments
    # parser.add_argument('--tag', action="store", dest="tag", type=str, required=True)
    given_args = parser.parse_args()  
    url = given_args.url 
    #tag = given_args.tag

main(url)