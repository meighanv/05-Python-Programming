"""
This program will test your knowledge of using Ctypes in python.
You should use ctype data types and ctype functions when possible

Steps:
   * You are provided with the POINT class that has two integers: x-coordinate and y-coordinate
   * Create a class RECT that represents a rectangle with two fields:  upperleft and lowerright 
   each of type POINT
   * The class RECT should have:
         - a constructor to initialize its corners
         - a method compute_Area to compute the area of the rectangle

   * Create a function quickSort (NOT part of the RECT class):
      - The quickSort function will take an array of integers (as an input parameter) and 
      sort the elements
      - the quickSort function should utilize ***libc.qsort*** to sort the items

"""
from ctypes import *
lib = cdll.LoadLibrary("libc.so.6")

class POINT(Structure):
      _fields_ = [("x", c_int),
                ("y", c_int)]

class RECT(Structure):
      _fields_ = [("lowerleft", POINT),
                  ("upperright", POINT)]
      def compute_Area(self):
          return (self.upperright.x - self.lowerleft.x) * (self.upperright.y - self.lowerleft.y) 
      

# def py_cmp_func(a, b):
#       print("py_cmp_func", a, b)
#       return 0

def quickSort(IntArray):
      ascending = lambda x, y: x.contents.value > y.contents.value
      CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
      cmp_func = CMPFUNC(ascending)
      lib.qsort(IntArray, len(IntArray), sizeof(c_int), cmp_func)
      for i in IntArray:
            print(i)
      return 0


# r1 = RECT(POINT(2, 2), POINT(7, 6))  # Area = 20
# r2 = RECT(POINT(1, 2), POINT(3, 4))  # Area = 4
# r3 = RECT(POINT(1, 3), POINT(4, 9))  # Area = 18
# r4 = RECT(POINT(3, 4), POINT(5, 8))  # Area = 8
# r5 = RECT(POINT(4, 6), POINT(7, 11)) # Area = 15

# IntArray5 = c_int * 5
# areas = IntArray5(r1.compute_Area(),
#                   r2.compute_Area(),
#                   r3.compute_Area(),
#                   r4.compute_Area(),
#                   r5.compute_Area())
# print("Hello")
# areasSorted = quickSort(areas)
# # for a in areasSorted:
# #       print(a)
