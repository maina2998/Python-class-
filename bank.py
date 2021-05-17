class BankAccount:
    Location ="Nairobi"
    def __init__(self,name,deposit,balance,account):
        self.name = name
        self.deposit = deposit
        self.balance = balance
        self.account = account

    def accepts_deposits(self):
        return f"{self.name} bank received my {self.accepts_deposits} every month"
    def  message(self):
        return f"I received my bank's {self.message} yesterday."
        
    

    