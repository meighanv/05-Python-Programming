"""
3. 
(The Triangle class) Design a class named Triangle that extends the
GeometricObject class defined below. The Triangle class contains:
    - Three float data fields named side1, side2, and side3 to denote the three
    sides of the triangle.
    - A constructor that creates a triangle with the specified side1, side2, and
    side3 with default values 1.0.
    - The accessor methods for all three data fields.
    - A method named getArea() that returns the area of this triangle.
    - A method named getPerimeter() that returns the perimeter of this triangle.
    - A method named __str__() that returns a string description for the triangle.
​
​
    class GeometricObject:
        def __init__(self, color = "green", filled = True):
            self.color = color
            self.filled = filled
​
        def getColor(self):
            return self.color
​
        def setColor(self, color):
            self.color = color
​
        def isFilled(self):
            return self.filled
​
        def setFilled(self, filled):
            self.filled = filled
    
        def toString(self):
            return "color: " + self.color + " and filled: " + str(self.filled)
​
​
    Write a test program that prompts the user to enter the three sides of the 
    triangle, a color, and 1 or 0 to indicate whether the triangle is filled. 
    The program should create a Triangle object with these sides and set the 
    color and filled properties using the input. The program should display the 
    triangle’s area, perimeter, color, and True or False to indicate whether the 
    triangle is filled or not.
    # Do this last

"""
import geometricObj
from math import sqrt

def main():
    # Collecting triangle data
    sides = getSides()
    color = input('What color is the triangle?\n')
    filled = fill()
    
    # creating Triangle object
    triangle = geometricObj.Triangle(color, filled, sides[0], sides[1], sides[2])
    print(triangle)

# Method to get the user input for sides
def getSides():
    # Empty list for side input
    sides = []
    # Collect input for each possible side of triangle
    for i in range(3):
        # Tracks whether or not valid input has been input
        valid = False
        while valid == False:
            try:
                # getting input for current side
                side = float(input(f'Please provide the length of side {i+1} for your triangle:\n'))
                valid = True
                sides.append(side)
            except ValueError:
                print('Error: Please provide a number value (ex: 5 or 5.3)!')
    # return the list of sides
    return sides

# Getting input for filled status with input validation
def fill():
    # Tracks whether or not valid input has been input
    valid = False
    while valid == False:
        try:
            # getting input for filled status
            validOptions = [0,1]
            fill = int(input('Would you like to fill this triangle? (1 = yes, 2 = no)\n'))
            while int(fill) not in validOptions:
                 fill = int(input('Incorrect input.\nWould you like to fill this triangle? (1 = yes, 2 = no)\n'))
            valid = True
            return fill
        except ValueError:
            print('Error: Please provide a number value (1 or 0)!')

main()
        