# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934
# Output : 37



def AddDigits(no):

    digit=0
    sum=0
    while no!=0:
        digit=no%10
        sum=sum+digit
        no=no//10
    return sum


def Main():
    no=int(input("Enter the Number: "))
    ret=AddDigits(no)

    print("Addition of {} number's digit is {}".format(no,ret))

if __name__=="__main__":
     Main()
