# This program creates five CellPhone objects and
# stores them in a list

import cellphone as c

def main():
    # Get a list of CellPhone
    phones = make_list()

    # Display the data in the list
    print('Here is the data you entered:')
    display_list(phones)

# The make_list function gets data from the user 
# for five phones. The function returns a list 
# of CellPhone Objects containing the data
def make_list():
    #Create empty list
    phone_list = []

    #Add five CellPhone objects to the list
    print('Enter data for five phones.')
    for count in range(1,6):
        #Get the phone data
        print('Phone number ' +str(count) +':')
        man = input('Enter the manufacturer:\n')
        mod = input('Enter the model number:\n')
        retail = float(input('Enter the retail price:\n'))
        print()

        phone = c.CellPhone(man,mod,retail)

        phone_list.append(phone)
    
    return phone_list

# The display_list function gets data from the list 
# passed as an argument. The function returns a list 
# of CellPhone Objects containing the data
def display_list(phone_list):
    for phone in phone_list:
        print('Manufacturer: ', phone.get_manufact())
        print('Model Number: ', phone.get_model())
        print(f'Retail Price: ${phone.get_retail_price():,.2f}')
        print()

main()