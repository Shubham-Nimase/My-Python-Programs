
# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.


import Arithmatic as Ar
def Main():
    no1=int(input("Enter the First Number: "))
    no2=int(input("Enter the Second Number: "))
    print()

    aret=Ar.Add(no1,no2)
    print("Addition of {} and {} is : {}".format(no1,no2,aret))

    sret=Ar.Sub(no1,no2)
    print("Substraction of {} and {} is : {}".format(no1, no2, sret))

    mret=Ar.Mult(no1,no2)
    print("Multiplication of {} and {} is : {}".format(no1,no2,mret))

    dret=Ar.Div(no1,no2)
    print("Division of {} and {} is : {}".format(no1,no2,dret))

if __name__=="__main__":
    Main()