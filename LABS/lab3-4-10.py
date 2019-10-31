#Defining Coefficient for the weight equation
COEFF = float(703)

#Defining main function
def main():
    bmi = calcBmi(float(input('Please provide the weight in pounds:')),
        float(input('Please provide the height in inches:')))
    
    overOrUnder(bmi)

#Function to take in mass(weight) and height to calculate BMI
def calcBmi(mass,height):
    return mass * COEFF/height**2

#Determine if numbers are overweight, underweight, or in acceptable range
def overOrUnder(ratio):
    #overweight range
    if ratio > 25:
        print("Overweight!")
    #underweight range
    elif ratio < 18.5:
        print("Underweight!")
    #Solid BMI range
    else:
        print("{:.2f} BMI is in the acceptable range.".format(ratio))


#calling main
main()