""" 4. Employee Class
    Write a class named Employee that holds the following data about an employee in attributes: 
    name, ID number, department, and job title.
    Once you have written the class, write a program that creates three Employee objects to
    hold the following data:
​
Name            ID Number       Department      Job Title
Susan Meyers    47899           Accounting      Vice President
Mark Jones      39119           IT              Programmer
Joy Rogers      81774           Manufacturing   Engineer
​
The program should store this data in the three objects and then display the data for each
employee on the screen. """

class Employee:
    # Defining Attributes of employee class
    def __init__(self):
        self.__name = ''
        self.__id = ''
        self.__dept = ''
        self.__title = ''

    # Configuring setters
    def set_name(self):
        self.__name = input('Provide the employee name: \n')

    def set_id(self):
        self.__id = input('Provide the employee ID number: \n')

    def set_dept(self):
        self.__dept = input('Provide the employee department: \n')

    def set_title(self):
        self.__title = input('Provide the employee job title: \n')

    # Configuring Getters
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_dept(self):
        return self.__dept

    def get_title(self):
        return self.__title 


""" # Define main function
def main():
    # Set employee object storage list
    employees = []

    # Iterate through three employee info entries
    for i in range(3):
        emp = Employee()
        emp.set_name()
        emp.set_id()
        emp.set_dept()
        emp.set_title()
        # Print extra line for spacing (visual user assist)
        print()
        # Append each completion of an employee record to 
        # the employees list
        employees.append(emp)

    # Header for displaying employee information
    print('Name:\t\tID:\t\tDepartment:\t\tTitle:')

    # Iterate through each record stored in employees list
    for emp in employees:
        # Print with same spacing as header
        print(f'{emp.get_name()}\t\t{emp.get_id()}\t\t{emp.get_dept()}\t\t{emp.get_title()}')

    print()

#Call main
#main() """