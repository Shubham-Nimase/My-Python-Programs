# Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.


class BankAccount:
    ROI = 10.5
    def __init__(self,name):
        self.Name = name
        self.Amount =0

    def Deposit(self):
        self.Amount = int(input("Enter amount: "))

    def Withdraw(self):
        Withdraw = int(input("Enter Withdraw amount: "))
        self.Amount = self.Amount - Withdraw

    def CalcilateIntrest(self):
        intrest = self.Amount*self.ROI/100
        print("Interest is: ",intrest)

    def Display(self):
        print("Bank Account name: ",self.Name)
        print("Bank Amount: ",self.Amount)


def main():

    name = input("Enter name: ")
    obj = BankAccount(name)
    obj.Deposit()
    obj.Withdraw()
    obj.CalcilateIntrest()
    obj.Display()


if __name__=="__main__":
    main()