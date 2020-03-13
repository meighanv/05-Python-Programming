"""
# Write a function binary_to_decimal that takes an integer containing 0s and 1s (i.e., a "binary" integer)
# and returns its decimal equivalent.
# For example, the decimal equivalent of binary 1101 is 13
# If the input value is not a binary number, the function should return "Invalid Input"
"""

def binary_to_decimal(binaryNumber):
    #Cast the int value as string
    string = str(binaryNumber)
    #Start try accept to handle value error
    try:
        #store the decimal value as a base 2 (binary) int
        decimal = int(string,2)
        # Unit test does not want ato convert negative numbers as they are represented differently in binary
        if decimal < 0:
            # Return invalid input if the decimal is less than 0 (negative)
            return f'Invalid Input'
        else:
            # Otherwise return the decimal value
            return decimal
    #In the case of int value containing anything other than 1's and 0's return 'Invalid Input'
    except ValueError:
        return f'Invalid Input'
