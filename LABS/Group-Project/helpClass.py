# This is a class to define the helpObject
# This should allow us to read in data from a text file and objectify it

class HelpObject:
    def __init__(self, desc, ex1, ex2, lib):
        self.__desc = desc
        self.__ex1 = ex1
        self.__ex2 = ex2
        # This is an attribute for the library associated with the help and examples
        self.__lib = lib

# Class settors
    def setDesc(self, desc):
        self.__desc = desc

    def setEx2(self, ex1):
        self.__ex1 = ex1
    
    def setEx1(self, ex2):
        self.__ex2 = ex2
    
    def setLib(self, lib):
        self.__lib = lib

# Class Gettors
    def getDesc(self):
        return self.__desc
    
    def getEx1(self):
        return self.__ex1
    
    def getEx2(self):
        return self.__ex2

    def getLib(self):
        return self.__lib