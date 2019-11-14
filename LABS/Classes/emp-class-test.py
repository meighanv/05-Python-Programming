import employees

def main():
    #worker = createWorker()
    #displayWorker(worker)
    supervisor = createSup()
    displaySup(supervisor)


def createWorker():
    name = input('What is the employee\'s name?\n')
    num = 0
    while num < 1:
        num = int(input('What is the employee\'s ID number?\n'))
    shift = 0
    while (shift < 1 and num > 2):
        shift = int(input('What is the employee\'s shift? (1: Day, 2: Night):\n'))
    pay_rate = 0.0
    while pay_rate < 1:
        pay_rate = float(input('What is the employee\'s pay rate (ex: 52.50)?\n'))   
    worker = employees.ProductionWorker(name, num, shift, pay_rate)
    return worker

def displayWorker(worker):
    print('\nEmployee Info:\n--------------\n')
    print('Name:\t', worker.get_name())
    print('Employee ID:\t', worker.get_number())
    shiftText = ''
    if worker.get_shift() == 1:
        shiftText = 'Day Shift'
    else:
        shiftText = 'Night Shift'
    print('Shift: ', shiftText)
    print('Pay Rate: {:.2f}'.format(worker.get_pay_rate()))

def createSup():
    name = input('What is the supervisor\'s name?\n')
    num = 0
    while num < 1:
        num = int(input('What is the supervisor\'s ID number?\n'))
    salary = -1.0
    while salary < 0.0:
        salary = float(input('What is the supervisor\'s salary?\n'))
    prod_bonus = 0.0
    while prod_bonus < 1:
        prod_bonus = float(input('What is the supervisor\'s production bonus?\n'))   
    worker = employees.ShiftSupervisor(name, num, salary, prod_bonus)
    return worker

def displaySup(worker):
    print('\nEmployee Info:\n--------------\n')
    print('Name:\t\t', worker.get_name())
    print('Employee ID:\t\t', worker.get_number())
    print('Salary:\t\t${:.2f}'.format(worker.get_salary()))
    print('Production Bonus:\t${:.2f}'.format(worker.get_prod_bonus()))
    print()
main()