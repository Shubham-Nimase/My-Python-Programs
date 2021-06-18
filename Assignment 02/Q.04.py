# Write a program which accept one number form user and return addition of its factors.
# Input :
# 12
# Output : 16
# (1+2+3+4+6)

def FactorsAdd(no):
    sum=0
    for i in range(1,int(no/2)+1,1):
        if no%i==0:
            sum=sum+i
    return sum

def Main():
    no=int(input("Enter the Number :"))
    fret=FactorsAdd(no)

    print("Addition of its factors is: ",fret)

if __name__=="__main__":
    Main()