# The BankAccount class simulates a bank account

class BankAccount:

    # The __init method acceps an argument for
    # the account's balance. It is assigned to 
    # the __balance attribute
    def __init__(self, balance):
        self.__balance = balance

    # The deposit method makes a deposit into the account
    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method makes withdraws from the account
    def withdraw(self, amount):
        if self.__balance >= float(amount):
            self.__balance -= float(amount)
        else:
            print('Error: Insufficient funds.')
    
    # Get the balance
    def get_balance(self):
        return self.__balance

    # The __str__ method returns a string
    # Indicating the object's state
    def __str__(self):
        return f'The balance is ${self.__balance:,.2f}'