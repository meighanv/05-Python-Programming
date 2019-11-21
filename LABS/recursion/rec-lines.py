"""
3. Recursive Lines
    Write a recursive function that accepts an integer argument, n. The function should display
    n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
    showing 2 asterisks, up to the nth line which shows n asterisks.
"""

def main():
    recLines(7)


def recLines(n):
    if n == 0:
        return 0
    else:
        print('*' + recLines(n-1)*'*')
        return n 
main()
