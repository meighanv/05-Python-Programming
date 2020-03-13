import ctypes, os
from ctypes import *

"""
This question will test your knowledge of using Ctypes and C-DLL in python. You should use Ctype data types and Ctype functions when possible
Steps:

•	Given "Sum.c" program that is used to produce "SumDLL.dll", you are required to:

  o	Create a method sum_numbers that takes an array of integers (as an input parameter) and return its sum

  o	The method sum_numbers should utilize sum_numbers from the given SumDLL.dll

###If performing this on a linux platform, may need to recompile the source into a *nix so###
- gcc -fPIC -c Sum.c
- gcc -shared -o libSum.so Sum.o

"""



def sum_numbers(numbers):
  # Load custom cdll after creating .so from orig C source
  libc = cdll.LoadLibrary("./libSum.so")
  # Cast original python list as c array
  arr = (ctypes.c_int * len(numbers))(*numbers)
  #return the result of shared library function to calling program
  return libc.sum_numbers(len(numbers), arr)

# nums = [1, 2, 4, 5, 7]
# print(sum_numbers(nums))

