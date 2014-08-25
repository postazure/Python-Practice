class BankAccount:
    def __init__(self):
        self.name = "Max"
        self.accountNumber = int(1001)
        self.balance = float(100)

    def __str__(self):
        msg = self.name + "'s Balance: $" + str(self.balance) + " Account Number: " + str(self.accountNumber)
        return msg

    def deposit(self, cashIn):
        self.balance = self.balance + cashIn
        

    def withdrawal(self, cashOut):
        self.balance = self.balance - cashOut
        

    def getBalance(self):
        return self.balance

class InterestAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)

    def setInterestRate(self, intRate):
        self.intRate = intRate

    def addInterest(self):
        
        self.balance = self.balance + (self.balance * (self.intRate / 100))
        print self.balance    
    
        

maxAccount = InterestAccount()
print maxAccount

depositAmt = float(raw_input("How much would you like to deposit? "))
maxAccount.deposit(depositAmt)
print maxAccount.balance

withdrawalAmt = float(raw_input("How much would you like to withdrawal? "))
maxAccount.withdrawal(withdrawalAmt)
print maxAccount.balance

intRate = float(raw_input("Interest Rate: "))
maxAccount.setInterestRate(intRate)
maxAccount.addInterest()
print maxAccount.balance

print maxAccount
