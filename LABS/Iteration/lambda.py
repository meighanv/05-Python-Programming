# Is a temporary function that you use. Used 
# once and cannot be called again. One-liner
# anonymous functions.
square = lambda x : x*x 
print(square(5))

sumnum = lambda x, y, z : x + y + z
print(sumnum(5, 10, 15))

from math import sqrt
quadPos = lambda a, b, c : (((-1*b)+sqrt((b**2)-(4*a*c)))/2*a)

print(quadPos(21,44,13))

quadNeg = lambda a, b, c : (((-1*b)-sqrt((b**2)-(4*a*c)))/2*a)
print(quadNeg(21,44,13))
