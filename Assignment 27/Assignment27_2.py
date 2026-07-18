class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Balance :", self.Amount)

    def Deposit(self):
        amt = float(input("Enter Deposit Amount: "))
        self.Amount += amt

    def Withdraw(self):
        amt = float(input("Enter Withdraw Amount: "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


obj1 = BankAccount("Mahadev", 10000)

obj1.Display()

obj1.Deposit()
obj1.Display()

obj1.Withdraw()
obj1.Display()

print("Interest =", obj1.CalculateInterest())

print()

obj2 = BankAccount("Rahul", 20000)

obj2.Display()

obj2.Deposit()
obj2.Withdraw()

print("Interest =", obj2.CalculateInterest())