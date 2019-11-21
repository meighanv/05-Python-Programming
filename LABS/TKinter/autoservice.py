class AutoService:
    def __init__(self, desc, cost):
        self.__desc = desc
        self.__cost = cost

    def setDesc(self,desc):
        self.__desc = desc

    def setCost(self,cost):
        self.__cost = cost 

    def getDesc(self):
        return self.__desc 

    def getCost(self):
        return self.__cost      