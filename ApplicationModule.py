from BankModule import Bank
from ChequingAccountModule import ChequingAccount
from SavingsAccountModule import SavingsAccount
class Application:
    def run(self):

        
        print(f'{"-"*30} ALL ACCOUNT INFORMATION {"-"*50}')
        print(f'{"-"*105}')
        items=[["S101","James Finch",222210212,"Savings",3400.99],["S102","Kell Forest",222214500,"Savings",42520.32],
        ["S103","Amy Stone   ",222212000,"Savings",8273.45],["C104","Kaitlin Ross",333315002,"Chequing",91230.45],["C105","Adem First",33333019,"Chequing",43987.67],
        ["C106","John Doe",333358927,"Chequing",34829.76]]

        print(" Customer ID             Name                Account Number         Type                  Balance         ")

        for i in items:
            print(":",i[0]," "*(16-len(i[0])),":",
            ":",i[1]," "*(16-len(i[1])),":",
            ":",i[2]," "*(16-len(str(i[2]))),":",
            ":",i[3]," "*(16-len(str(i[3]))),":",
            ":",i[4]," "*(16-len(str(i[4]))),":")
        
        print(f'{"-"*105}')
        print(f'{"-"*105}')

        sav1=SavingsAccount("S101","James Finch",222210212,3400.90)
        Bank.s_accountList.append(sav1)

        print(f'Trying to withdraw $500.00 from the following account')
        print(f'S101 \t James Finch \t 222210212 \t Savings \t 3400.90')
        Bank.s_accountList[0].withdraw(500.00)
        print(f'{"-"*105}')



        print(f'{ "-" * 105}')
        sav2=SavingsAccount("S102","Kell Forest",222214500,42520.32)
        Bank.s_accountList.append(sav2)

        print(f'Trying to deposit $-250.00 to the following account')
        print(f'S102 \t Kell Forest \t 222214500 \t Savings \t 42520.32')
        Bank.s_accountList[1].deposit(-250.00)
        print(f'{ "-" * 105}')



        print(f'{ "-" * 105}')
        
        sav3=SavingsAccount("S103","Amy Stone",222212000,8273.45)
        Bank.s_accountList.append(sav3)

        print(f'Trying to withdraw $10000.00 to the following account')
        print('S103 \t Amy Stone \t 222212000 \t Savings \t 8273.45')
        Bank.s_accountList[2].withdraw(10000.00)
        print(f'{ "-" * 105}')


        print(f'{ "-" * 105}')
        sav4=SavingsAccount("S103","Amy Stone",222212000,8273.45)
        Bank.s_accountList.append(sav4)

        print(f'Trying to deposit $5000.00 to the following account')
        print('S103 \t Amy Stone \t 222212000 \t Savings \t 8273.45')
        Bank.s_accountList[3].deposit(5000.0)
        print(f'{ "-" * 105}')
       

        cheq1=ChequingAccount("C104","Kaitlin Ross",333315002,91230.45)
        Bank.s_accountList.append(cheq1)

        print(f'{ "-" * 105}')
        print(f'Trying to deposit $7300.00 to the following account')
        print(f'C104 \t Kaitlin Ross \t 333315002 \t Chequing  \t 91230.45')
        Bank.s_accountList[4].deposit(7300.00)
        print(f'{ "-" * 105}')


        cheq2=ChequingAccount("C105","Adem First",333303019,43987.67)
        Bank.s_accountList.append(cheq2)

        print(f'{ "-" * 105}')
        print(f'Trying to withdraw $45000.40 from the following account')
        print(f'C105 \t Adem First \t 333303019 \t Chequing \t 43987.67')
        Bank.s_accountList[5].withdraw(45000.40)
        print(f'{ "-" * 105}')

        cheq3=ChequingAccount("C106","John Doe",333358927,34829.76)
        Bank.s_accountList.append(cheq3)


        print(f'{ "-" * 105}')
        print(f'Trying to withdraw $37000.00 from the following account')
        print(f'C106 \t John Doe \t 333358927 \t Chequing \t 34829.76')
        Bank.s_accountList[6].withdraw(37000.00)
        print(f'{ "-" * 105}\n')

        print(f'{"-"*30} ALL ACCOUNT INFORMATION {"-"*50}')
        print(f'{"-"*105}')
        print(" Customer ID               Name                   Account Number               Type               Balance         ")
        print(f'{"-"*105}')

        sav5=SavingsAccount("S647","Alex Du",222290192,4783.98)
        Bank.s_accountList.append(sav5)

        cheq5=ChequingAccount("C567","Dale Stayne",333312312,12894.56)
        Bank.s_accountList.append(cheq5)


        Bank.s_accountList.remove(sav3)
        newItems=[]
        newItems=Bank.s_accountList
        for j in newItems:
            print(j,end="\t\t\t\n")


app=Application()
app.run()

