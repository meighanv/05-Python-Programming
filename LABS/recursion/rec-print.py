"""
1. Recursive Printing
    Design a recursive function that accepts an integer argument, n, and prints the numbers 1
    up through n.
"""

def recPrint(n):
    if n > 0:
        (recPrint(n-1))
        print(n)
        return n

def main():
    recPrint(5)

main()