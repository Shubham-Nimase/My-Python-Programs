# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934
# Output : 7

def CountDigit(no):

    icnt=0

    if no==0:
        return 1

    while no != 0:
        icnt=icnt+1
        no = no // 10;
    return icnt;

def Main():
    no=int(input("Enter the Number: "))
    ret=CountDigit(no)

    print("Number of Digits are: ",ret)

if __name__=="__main__":
    Main()