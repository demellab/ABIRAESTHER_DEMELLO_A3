class Error(Exception):
    pass

class Insufficient_Balance_Error(Error):
    def __str__(self):
        return "A New Excpetion occurred: Insufficient Balance in your account, Cannot withdraw "

    
class Minimum_Balance_Error(Error):
    def __str__(self) :
        return "A New Excpetion occurred: You must maintain a minimum balance of $3000 in your Savings account."


class Incorrect_Amount_Error(Error):
    def __str__(self):
        return "A New Excpetion occurred: You have to provide a positive number for an amount to be deposited! "


class Overdraft_Limit_Error(Error):
    def __str__(self):
        return "A New Excpetion occurred: Overdraft Limit exceeded. You can only use $2000 from overdraft"

    


            