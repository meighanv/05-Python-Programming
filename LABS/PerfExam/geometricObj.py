from math import sqrt

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color
        
    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled

    def toString(self):
        return "color: " + self.color + " and filled: " + str(self.filled)

class Triangle(GeometricObject):
    
    def __init__(self, color = "green", filled = True, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__(color,filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    # mutators
    def set_side1(self, side1):
        self.__side1 = side1

    def set_side2(self, side2):
        self.__side2 = side2
    
    def set_side3(self, side3):
        self.__side3 = side3 

    # Accessors
    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3
    
    # Triangle Math functions 
    # Triangle Perimeter
    def getPerimeter(self):
        return self.get_side1()+self.get_side2()+self.get_side3()
    
    # Triangle Area
    def getArea(self):
        p = self.getPerimeter()/2
        area = sqrt(p*(p-self.__side1)*(p-self.__side2)*(p-self.__side3))
        return area

    ## __str__ method
    def __str__(self):
        # Converting filled integer value to the appropriate string
        if self.filled == 1:
            filled = 'True'
        else:
            filled = 'False'
        # Checking Triangle validity before returning triangle data to user. 
        if self.getArea() == 0:
            return f'A triangle with sides of {self.__side1}, {self.__side2}, and {self.__side3} is not valid. Goodbye!'
        else:
            return f'\nTriangle sides:\n{self.__side1}, {self.__side2}, {self.__side3}\n\nPerimeter: {self.getPerimeter()}\nArea: {self.getArea()}\n\nColor: {self.color}\nFilled: {filled}'