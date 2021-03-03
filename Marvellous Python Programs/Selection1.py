import MarvellousNumbers as MN
# import MarvellousNumbers
# from MarvellousNumbers import CheckEven
# from MarvellousNumbers import *
        
def main():
    print("Enter one number")
    value = int(input())
    
    bret = MN.CheckEven(value)

    if bret == True:
        print("{} is Even number".format(value))
    else:
        print("{} is Odd number".format(value))
        
if __name__ == "__main__":
    main()


# Camel case            checkEevn()
# Hungarian case      CheckEven()
# Student case          fun()

# iret
# fret
# lret

