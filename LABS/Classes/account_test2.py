# This program demos the BankAccount class
import bankaccount

def main():
    # get the starting balance 
    start_bal = float(input('Enter your starting balance:\n'))

    # Instantiate bank account
    savings = bankaccount.BankAccount(start_bal)

    #Deposit the users paycheck
    pay = float(input('How much were you paid this week?\n'))
    print('I will deposit this in your account')
    savings.deposit(pay)
    
    #Display the balance
    print(savings)

    #Withdraw cash
    cash = input('How much would you want to withdraw?\n')
    print('I will with draw this from your account.')
    savings.withdraw(cash)
    
    #Display the balance
    print(savings)

main()