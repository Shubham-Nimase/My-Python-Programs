#
# Write a program which contains one class named as Arithmetic.
#
# Arithmetic class contains two instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.
#
# There are five instance methods inside class as Accept(), Addition(), Subtraction(),
# Multiplication(), Division().
#
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
#
# After designing the above class call all instance methods by creating multiple objects.


class Arithmatic:

    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        self.value1 = int(input("Enter first value :"))
        self.value2 = int(input("Enter Second value :"))

        ret=self.Addition(self.value1,self.value2)
        print("Addition of Values is: ",ret)

        ret = self.Substraction(self.value1, self.value2)
        print("Substraction of Values is: ", ret)

        ret = self.Multiplication(self.value1, self.value2)
        print("Multiplication of Values is: ", ret)

        ret = self.Division(self.value1, self.value2)
        print("Division of Values is: ", ret)




    def Addition(self,value1,value2):
        return value1+value2;

    def Substraction(self,value1,value2):
        return value1-value2;

    def Multiplication(self,value1,value2):
        return value1 * value2;

    def Division(self,value1,value2):
        return value1/value2;




def main():
    obj = Arithmatic()
    obj.Accept()

if __name__=="__main__":
    main()

