# Write a program which accept one number from user and return its factorial.
# Input :
# 5
# Output : 120


def Factorial(no):
    Fact=1
    for i in range(no,0,-1):
        Fact=Fact*i
    return Fact


def Main():
    no=int(input("Enter the Number :"))

    fret=Factorial(no)
    print("It,s Factorial is {}".format(fret))

if __name__=="__main__":
    Main()