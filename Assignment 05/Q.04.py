# Write a recursive program which accept number from user and return
# summation of its digits.
# Input : 879
# Output : 24

sum=0

def SumDigit(no):
    global sum
    if no!=0:
        digit=no%10
        sum=sum+digit
        no=no//10
        SumDigit(no)
    return sum

def main():
    no=int(input("ENter the Number: "))
    ret=SumDigit(no)
    print("Summation of Digits is:",ret)

if __name__=="__main__":
    main()