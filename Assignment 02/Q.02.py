# Write a program which accept one number and display below pattern.
# Input :
# 5
# Output : *  *  *  *  *
#          *  *  *  *  *
#          *  *  *  *  *
#          *  *  *  *  *
#          *  *  *  *  *



def Pattern(no):
    for i in range(0,no,1):
        for j in range(0,no,1):
            print("*",end="     ")
        print()

def Main():
    no=int(input("Enter the Number: "))
    Pattern(no)
    pass

if __name__=="__main__":
    Main()