#Miles per gallon calculator
#Asking user for miles driven and gas used
milesDriven = input('Provide miles driven:\n')
gasUsed = input('Provide gallons of gas used:\n')

mpg = float(milesDriven)/float(gasUsed)     

print('The miles used per gallon was {:.2f}'.format(mpg))