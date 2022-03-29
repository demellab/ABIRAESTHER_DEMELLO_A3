from SavingsAccountModule import SavingsAccount
from ChequingAccountModule import ChequingAccount

class Bank:
    s_accountList=[]

    @staticmethod
    def __init__():
        #accountList=[]
        Bank.s_accountList=[]
        # Bank.s_accountList.append(SavingsAccount("S101", "James Finch", 222210212, 3400.99))
        Bank.s_accountList.append(SavingsAccount("S102","Kell Forest", 222214500, 42520.32))
        Bank.s_accountList.append(SavingsAccount("S103","Amy Stone", 222212000, 8273.45))
        Bank.s_accountList.append(SavingsAccount("S103","Amy Stone", 222212000, 8273.45))
        
        # Bank.s_accountList.append(ChequingAccount("C104", "Kaitlin Ross", 333315002, 91230.45))
        Bank.s_accountList.append(ChequingAccount("C105", "Adem First", 333303019, 43987.67))
        # Bank.s_accountList.append(ChequingAccount("C106", "John Doe", 333358927, 34829.76))

    @staticmethod
    def showAll():
        Bank.s_accountList=[]

