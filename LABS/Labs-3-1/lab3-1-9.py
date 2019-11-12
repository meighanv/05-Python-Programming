#defining constant coefficient
COEFF = float(9/5)

#getting user input for Celcius temp
c = float(input('Provide the Celcius temperature to convert to Fahrenheit:\n'))

#Calculating Fahrenheit
f = COEFF*c + 32

#printing result
print('{} Celcius is {:.2f} Fahrenheit.'.format(c,f))
