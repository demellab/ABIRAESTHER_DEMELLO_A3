from AccountExceptions import Insufficient_Balance_Error
from AccountExceptions import Minimum_Balance_Error
from AccountExceptions import Incorrect_Amount_Error
from AccountModule import Account

class SavingsAccount(Account):

    def __init__(self,customerID:complex, name:str, accNo:int, balance=0.0):
        super().__init__(customerID,name,accNo)
        self.__balance=balance
        

    def withdraw(self, AmountToWithdraw:float):
        super().withdraw(AmountToWithdraw)
        
        try:
            if AmountToWithdraw>self.__balance:
                raise Insufficient_Balance_Error
            elif (self.__balance-AmountToWithdraw) <3000:
                raise Minimum_Balance_Error
            else:
                self.__balance= self.__balance - AmountToWithdraw
                print(f"Successfully withdrawn ${AmountToWithdraw} from the Account Number:{super().getID()}\n Balance left in Savings Account after withdrawal is ${self.__balance}")

        except Insufficient_Balance_Error as insuf:
            print(insuf)

        except Minimum_Balance_Error as min:
            print(min)


    def deposit(self,AmountToDeposit:float):
        super().deposit(AmountToDeposit)

        try:
            if AmountToDeposit<=0:
                raise Incorrect_Amount_Error
            else:
                self.__balance = self.__balance + AmountToDeposit
                print(f"Successfully deposited ${AmountToDeposit} to the Account Number: {super().getID()}\nBalance left in Savings Account after deposit is: ${self.__balance}")
            


        except Incorrect_Amount_Error as incorrect:
            print(incorrect)


    def __str__(self):
        return f"{super().__str__()}            Savings               {self.__balance:.2f}"






