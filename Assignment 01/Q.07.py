# Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8
# Output : False
# Input : 25
# Output : True


def Divisible(no):

    if no%5==0:
        return True
    else:
        return False

def Main():
    no=int(input("ENter the number : "))
    ret=Divisible(no)

    if ret==True:
        print("{} is divisible by 5".format(no))
    else:
        print("{} is Not divisible by 5".format(no))

if __name__=="__main__":
    Main()