# import Arithematic

#import Arithematic as XYZ

#from Arithematic import Addition,Substraction

from Arithematic import *

# Entry point function
def main():
    print("__name__ from main is : ",__name__)
    print("Enter first number : ")
    value1 = int(input())
    
    print("Enter second number : ")
    value2 = int(input())
    
    ret1 = Addition(value1,value2)
    ret2 = Substraction(value1,value2)
    
    print("Addition is :",ret1)
    print("Substraction is : ",ret2)

# Code starter
if __name__ == "__main__":
    main()
