"""
# Write a function binary_to_decimal that takes an integer containing 0s and 1s (i.e., a "binary" integer)
# and returns its decimal equivalent.
# For example, the decimal equivalent of binary 1101 is 13
# If the input value is not a binary number, the function should return "Invalid Input"
"""

def binary_to_decimal(binaryNumber):
    #Converting the int value to string
    string = str(binaryNumber)
    try:
        decimal = int(string,2)
        if decimal < 0:
            return f'Invalid Input'
        else:
            return decimal
    except ValueError:
        return f'Invalid Input'
