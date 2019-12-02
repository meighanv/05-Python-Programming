import time

def displayMenu():

    valid_choice = ['os', 'sys']

    print("Welcome to the Python Library Help System, please\nchoose one of the following libraries (q to quit):")
    
    #keep user in while loop until they make a valid selection
    while True:
        try:
            
            #ask user for input at beginning of loop
            user_choice = input("os, sys\n>").lower()
            
            if user_choice in valid_choice:
                print("Taking you to the", user_choice, "help page!")
               
                #using time.sleep gives user time to read validation message
                time.sleep(1)
                displaySelection(user_choice)
            elif user_choice == 'q':
                break
            else:
                continue
        except ValueError:
            print("You entered something weird.")

def displaySelection(uc):
    pass

displayMenu()