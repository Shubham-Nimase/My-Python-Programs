# Write a program which accept number from user and print that number of “*” on screen.
# Input : 5
# Output : * * * * *



def Display(no):
    for i in range(0,no,1):
        print("*",end="     ")
    print()

def Main():
    no=int(input("ENter the Number :"))

    Display(no)

if __name__=="__main__":
    Main()


