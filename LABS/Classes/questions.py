import pickle

class Question:
    def __init__(self):
        self.__question = ''
        self.__answer1 = ''
        self.__answer2 = ''
        self.__answer3 = ''
        self.__answer4 = ''
        self.__correct = ''

    def set_question(self, statement):
        self.__question = statement

    def set_answer1(self, statement):
        self.__answer1 = statement

    def set_answer2(self, statement):
        self.__answer2 = statement
    
    def set_answer3(self, statement):
        self.__answer3 = statement
    
    def set_answer4(self, statement):
        self.__answer4 = statement
    
    def set_correct(self, statement):
        self.__correct = statement

    def get_question(self):
        print(f'{self.__question}')

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correct(self):
        return self.__correct

""" def writeData(data, filename):
    #Opens the file on disk for writing
    q_file = open(filename, 'wb')
    #Dump data to file
    pickle.dump(data, q_file)
    #close file
    q_file.close() """

""" qbank = []

filename = 'qbank.dat'

for i in range(10):
    q = Question()
    statement = input('Give question:\n')
    q.set_question(statement)
    statement = input('Give answer1:\n')
    q.set_answer1(statement)
    statement = input('Give answer2:\n')
    q.set_answer2(statement)
    statement = input('Give answer3:\n')
    q.set_answer3(statement)
    statement = input('Give answer4:\n')
    q.set_answer4(statement)
    statement = input('Give correct answer:\n')
    q.set_correct(statement)
    qbank.append(q)

writeData(qbank, filename)

 """