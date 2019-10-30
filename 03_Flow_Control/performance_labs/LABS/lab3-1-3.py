#Defining CONSTANT for feet in acres
FEET_IN_ACRES = 43560

#gathering input and storing the feet into a variable
feet = int(input("Provide the total amount of square feet:"))

#Calculate and print using int type for feet and 
#float type for calculation of acres
print('The total acres from {:d} is {:f}'.format(feet, (float(feet)/FEET_IN_ACRES)))