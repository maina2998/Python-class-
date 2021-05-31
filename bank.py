from datetime import datetime

class BankAccount:
    Location ="Nairobi"
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        self.balance = 0
        self.borrow=0
        self.statement = []


    def accepts_deposits(self):
        return f"{self.name} bank received my {self.accepts_deposits} every month"
    def  message(self):
        return f"I received my bank's {self.message} yesterday."
    def show_balance(self):
        return f"Hello {self.name} your balance is {self.balance}"  
    def deposit(self,amount):
            if amount>0:
                self.balance += amount
                now = datetime.now()
                transaction={
                    "amount":100000,
                    "time":now,
                    "Narration":"You deposited",
                }
                self.statement.append(transaction),
                return self.show_balance()
    

            else:
                return f"You cannot withdraw {self.balance}"
    def withdraw(self,amount):
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


           



        
    

    