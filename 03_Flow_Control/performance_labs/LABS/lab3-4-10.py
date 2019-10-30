#Defining Coefficient for the weight equation
COEFF = float(703)

#Defining main function
def main():
    bmi = calcBmi(float(input('Please provide the weight in pounds:')),
        float(input('Please provide the height in inches:')))
    
    overOrUnder(bmi)

def calcBmi(mass,height):
    return mass * COEFF/height**2

def overOrUnder(ratio):
    if ratio > 25:
        print("Overweight!")
    elif ratio < 18.5:
        print("Underweight!")
    else:
        print("{:.2f} BMI is in the acceptable range.".format(ratio))


#calling main
main()