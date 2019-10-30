#Defining Coefficient for the weight equation
COEFF = float(9.8)

#Defining main function
def main():
    weight = calcWeight(float(input('Please provide the mass of the object:')))
    heavyOrLight(weight)

def calcWeight(mass):
    return mass * COEFF

def heavyOrLight(newtons):
    if newtons > 1000:
        print("Too heavy!")
    elif newtons < 10:
        print("Too light.")
    else:
        print("{:.2f} newtons is in the acceptable range.".format(newtons))


#calling main
main()