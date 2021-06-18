# Write a program which accept one number and display below pattern.
# Input :
# 5
# Output :
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

def Pattern(no):
    for i in range(0,no+1,1):
        for j in range(1,no+1,1):
            if i>=j:
                print(j,end="    ")
        print()

def Main():
    no=int(input("Enter the Number: "))
    Pattern(no)

if __name__=="__main__":
    Main()