# Write a program which contains one class named as Numbers.

# Numbers class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.

# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),Factors().

# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.

# After designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self,no):
        self.Value = no

    def ChkPrime(self):
        flag = True
        j = int(self.Value / 2)

        for i in range(2, (j + 1)):
            if self.Value % i == 0:
                flag = False
                break
        return flag

    def ChkPerfect(self):

        j=int(self.Value/2)
        sum=0
        for i in range(1,(j+1)):
            if self.Value % i == 0:
                sum=sum+i
        if sum == self.Value:
            return  True
        else:
            return False



    def Factors(self):

        j= int(self.Value/2)
        for i in range(1,j+1):
            if self.Value % i == 0:
                print(i)

    def SumFactor(self):

        j = int(self.Value/2)
        sum = 0
        for i in range(1,j+1):
            if self.Value % i == 0:
                sum = sum + i
        print("Sum Factor is:",sum)


def main():

    no = int(input("Enter the Number: "))
    obj = Numbers(no)

    ret = obj.ChkPrime()
    if ret == False:
        print("It is not prime number")
    else:
        print("It is prime number")

    ret = obj.ChkPerfect()
    if ret == False:
        print("It is not perfect number")
    else:
        print("It is perfect number")

    obj.Factors()
    obj.SumFactor()


if __name__=="__main__":
    main()