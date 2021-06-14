from datetime import datetime

class BankAccount:
    Location ="Nairobi"
    def __init__(self,name,phone_number,loan):
        self.name = name
        self.loan=loan
        self.phone_number = phone_number
        self.statement = []
      
      
        


    def accepts_deposits(self):
        return f"{self.name} bank received my {self.accepts_deposits} every month"
    def  message(self):
        return f"I received my bank's {self.message} yesterday."
    def show_balance(self):
        return f"Hello {self.name} your balance is {self.balance}"  
    def deposit(self,amount):

        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"

        if amount<0:
            return f"You cannot deposit {self.deposit} "
        else:        
                self.balance += amount
                now = datetime.now()
                transaction={
                    "amount":100000,
                    "time":now,
                    "Narration":"You deposited",
                }
                self.statement.append(transaction),
        return self.show_balance

    def withdraw(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"

        if amount>self.balance:
                return f"Your balance is {self.balance} you cannot withdraw {amount}"
        else:
                self .balance -= amount 
                now = datetime.now()
                transaction={
                    "amount":100000,
                    "time":now,
                    "Narration":"You deposited",
                }
                self.statement.append(transaction),
                return self.show_balance()
    def loan(self,amount): 
        return f"Your amount is {amount}"           
    def repayloan(self,amount):
        return f"Your amount is {amount}"  

    def show_statement(self):  
        return self.statement
    def show_statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration = transaction["Narration"]
            time = transaction["time"]
            date = time.strftime("%d/%m/%y")
            print(f"{date}:{Narration} {amount}")
        return 
    def borrow(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"
        if amount < 0:
             return "You can't borrow"
        elif  self.loan >0:
            return "You have an existing loan"
        elif amount <0.1*self.balance:
             return "You not qualified for any loan"   
        else:
             loan = amount * 1.05
             self.loan = loan 
             self.balance += amount
             self .balance -= amount 
             now = datetime.now()
             transaction={
                    "amount":amount,
                    "time":now,
                    "Narration":"You have borrowed",
                }
             self.statement.append(transaction),
             return f"{self.show_balance()} your loan is not complete"
    def repay(self,amount):

        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"

        if amount< 0:
            return "You have to pay your loan"
        elif amount <self.loan:
            self.loan-=amount
            return "Hello your loan has not been cleared"
        else:
            diff = amount - self.loan
            self.loan =0
            self.deposit(diff) 
            now = datetime.now()
            transaction={
                    "amount":amount,
                    "time":now,
                    "Narration":"You have repayed",
                }
            self.statement.append(transaction),
            return f"{self.show_balance()} your loan is completely sorted"


    def transfer(self,account,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"
        fee=amount*0.05
        total =amount + fee

        if amount > 0:
            return f"your balance is {self.balance} and you need at least{total} for this transfer "   
        else:
            return "You cannot transfer this amount"


class MobileMoneyAccount(BankAccount):
    def __init__ (self,name,phone_number,service_provider):
        BankAccount .__init__ (name,phone_number)
        self.service_provider=service_provider
    def buy_airtime(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"
        if amount >0:
            return f"Dear customer you have successfully purchase the airtime"
        elif self.balance>amount:
            return f"Dear customer your balance is low to purchase this airtime"   
        else:
            self.balance=self.balance-amount
            return f"Dear customer, You can buy airtime.Your balance is {amount}"

    def withdraw(self,amount):
        try:
            1000 + amount
        except TypeError:
            return f"The amount must be in figures"
        if amount > 0:
            return f""
        if amount >0:
            return f"Dear customer you have successfully purchase the airtime"
        elif self.balance>amount:
            return f"Dear customer your balance is low to purchase this airtime"   
        else:
            self.balance=self.balance-amount
            return f"Dear customer, You can buy airtime.Your balance is {amount}"
    



          




    