# Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11
# Output : Positive Number
# Input : -8
# Output : Negative Number
# Input : 0
# Output : Zero



def ChkNO(no):

    if no<0:
        return False
    elif no>0:
        return True
    else:
        return -1

def Main():
    no=int(input("Enter the Number: "))
    bret=ChkNO(no)

    if bret==True or bret==False:
        if bret==True:
            print("{} is Positive Number".format(no))
        else:
            print("{} is Negative Number".format(no))
    else:
        print("It's Zero")


if __name__=="__main__":
    Main()
