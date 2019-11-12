# This program tests the CellPhone class

import cellphone as c

def main():
    # Get the phone data
    man = input('Enter the manufacturer:\n')
    mod = input('Enter the model number:\n')
    retail = float(input('Enter the retail price:\n'))

    # Create an instance of the CellPhone class
    phone = c.CellPhone(man, mod, retail)

    # Display the data that was entered
    print('Here is the data that you entered:')
    print('Manufacturer: ', phone.get_manufact())
    print('Model Number: ', phone.get_model())
    print(f'Retail Price: ${phone.get_retail_price():,.2f}')
    
#Call Main
main()