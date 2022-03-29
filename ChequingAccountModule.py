from AccountModule import Account
from AccountExceptions import Overdraft_Limit_Error
from AccountExceptions import Incorrect_Amount_Error
from CustomerModule import Customer

class ChequingAccount(Account):
    def __init__(self,customerID:complex, name:str, accNo:int, balance=0.0):
        super().__init__(customerID,name,accNo)
        self.__balance=balance
        
    
    def withdraw(self, AmountToWithdraw:float):
        super().withdraw(AmountToWithdraw)

        try:
            if AmountToWithdraw > (2000+self.__balance):
                raise Overdraft_Limit_Error
            else:
                self.__balance = self.__balance- AmountToWithdraw
                print(f"Successfully withdrawn {AmountToWithdraw} from the account number {super().getID()} \n The balance in the Chequing Account after withdrawal is ${self.__balance}")

        except Overdraft_Limit_Error as over:
            print(over)

    def deposit(self, AmountToDeposit:float):
        super().deposit(AmountToDeposit)

        try:
            if AmountToDeposit<=0:
                raise Incorrect_Amount_Error
            else:
                self.__balance = self.__balance+ AmountToDeposit
                print(f"Successfully deposited ${AmountToDeposit} to the Account Number: {super().getID()} \n The balance in the Chequing account after deposit is ${self.__balance}")

        except Incorrect_Amount_Error as incorrect:
            print(incorrect)

    def __str__(self):
        return f"{super().__str__()}               Chequing               {self.__balance:.2f}"


