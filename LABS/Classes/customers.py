import persons

def main():
    customer = createCustomer()
    printCustomer(customer)
    
def createCustomer():    
    name = input('Provide a customer name:\n')
    address = input('Provide customer address:\n')
    number = input('Provide a 10-digit phone number (no dashes, spaces, or other punctuation):\n')
    while number.isnumeric() == False:
        number = input('Invalid input. Provide a 10-digit phone number (no dashes, spaces, or other punctuation):\n')
    opt_in = input('Are they subscribed to the email program? (Y/N)\n')
    while opt_in.upper() not in ['Y','N']:
        opt_in = input('Invalid option. Are they subscribed to the email program? (Y/N)\n')
    if opt_in == 'Y':
        opt_in = True
    else:
        opt_in = False
    
    cust = persons.Customer(name, address, number, opt_in)
    return cust

def printCustomer(customer):
    print('Name:\t', customer.get_name())
    print('Address:\t', customer.get_address())
    print('Phone:\t', customer.get_number())
    if customer.get_opt_in == True:
        print('Subscribed:\tYes')
    else: 
        print('Subscribed:\tNo')

main()