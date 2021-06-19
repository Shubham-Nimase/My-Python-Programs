
# Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1 ,no2.
# That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance variables.
#
# Initialise instance variable in init method by accepting the values from user.
#
# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
#
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()



class Demo:
    value = 22

    def __init__(self,n,m):
        self.no1 = n
        self.no2 = m


    def Fun(self):
        print("Value of no1 is: ",self.no1)

    def Gun(self):
        print("Value of no2 is: ",self.no2)



def main():

    no1 = int (input("Enter first Number: "))
    no2 = int (input("Enter Second Number: "))

    obj1 = Demo(no1,no2)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()

if __name__=="__main__":
    main()

