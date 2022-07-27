
class Account:
    balance=0
    def __init__(self,id,name,balance):
        self.id=id
        self.name=name
        self.balance=balance
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getBalance(self):
        return self.balance
    def Credit(self,amount):
        self.balance += amount
        return self.balance
    def debit(self,amount):
        if(amount <= self.balance):
            self.balance -= amount
            return self.balance
        else:
            print("Amount exceed balance \n")
            return self.balance
    def TransferTo(self,amount,Account):
        if(amount <= self.balance):
            amount=Account
        else:
            print("Amount exxceed balance \n")
            return self.balance
    def Info(self):
        print(f" ID = {self.id} \n Name is = {self.name} \n Balance is {self.balance} ")
 
acc=Account(19102616,"Abdelramhan Nasr", 500000)
acc.Info()
print(f"the credit is {acc.Credit(100)} \n and the debit is {acc.debit(200)} ")
