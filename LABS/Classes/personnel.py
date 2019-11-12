class PersonInfo:
    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__age = 0
        self.__phoneNum = ''
    
    def set_name(self):
        self.__name = input('Provide the person\'s name:\n')
    
    def set_address(self):
        self.__address = input('Provide the person\'s address:\n')
    
    def set_age(self):
        self.__age = input('Provide the person\'s age:\n')
    
    def set_phoneNum(self):
        self.__phoneNum = input('Provide the person\'s phone number:\n')

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phoneNum(self):
        return self.__phoneNum

#def main():
personnel = []
for i in range(1,3):
    person = PersonInfo()
    person.set_name()
    person.set_address()
    person.set_age()
    person.set_phoneNum()
    personnel.append(person)
for i in personnel:
    print(f'Name: {i.get_name()} ')
    print(f'Address: {i.get_address()} ')
    print(f'Age: {i.get_age()} ')
    print(f'Phone: {i.get_phoneNum()} ')
    print()

#main()
