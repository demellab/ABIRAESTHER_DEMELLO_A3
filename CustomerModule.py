class Customer:
    def __init__(self,customerID:complex, name:str):
        self.__id=customerID
        self.__name=name

    def setID(self,customerID):
        self.__id=customerID
    def getID(self):
        return self.__id
    
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def __str__(self) :
        return f"{self.__id}                  {self.__name}           "
    
