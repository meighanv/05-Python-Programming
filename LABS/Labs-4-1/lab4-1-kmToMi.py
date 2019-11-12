#Setting the equation coefficient for KM conversion to miles
COEFF = 0.6214

def main():
    km = getKm()
    print('The number of miles in {:.2f} kilometers is {:.2f}'.format(km,kmToMi(km)))

#defining function to get the miles while incorporating some input validation
def getKm():
    miles = int(input('Please provide the # of kilometers to convert:\n'))
    while miles < 1 or str(miles).isnumeric() == False:
        miles = int(input('Invalid input. Please provide the # of kilometers to convert:\n'))
    return miles

#defining function to make the calculation.
def kmToMi(km):
    return float(km) * COEFF

main()