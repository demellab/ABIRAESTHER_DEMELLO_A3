from abc import abstractmethod
from CustomerModule import Customer

class Account(Customer):
    def __init__(self, customerID:complex, name:str,accNo:int):
        super().__init__(customerID,name)
        self.__accountNum=accNo


    @abstractmethod
    def withdraw(self, AmountToWithdraw:int):
        pass

    @abstractmethod
    def deposit(self,AmountToDeposit:int):
        pass
    
    def __str__(self):
        return f"{super().__str__()}            {self.__accountNum}"

