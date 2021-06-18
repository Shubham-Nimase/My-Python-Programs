# Write a program which accept one number from user and check whether number is prime or not.
# Input :
# 2
# Output : It is Prime Number


def ChkPrime(no):

    # for i in range(2,no,1):
    #     if no%i==0:
    #         return False
    #     else:
    #         return True

    ret=True
    j=int(no/2)
    for i in range(2,(j+1)):
        if no%i==0:
            ret= False
            break
    return ret

def Main():
    no=int(input("Enter the Number :"))
    bret=ChkPrime(no)

    if bret==True:
        print("{} is Prime Number.".format(no))
    else:
        print("{} is NOT Prime Number.".format(no))


if __name__=="__main__":
    Main()




