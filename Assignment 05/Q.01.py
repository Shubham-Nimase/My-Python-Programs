# Write a recursive program which display below pattern.
# Input : 5
# Output : * * * * *


def DisplayPattern(no):
    if no>0:
        print("*",end=" ")
        no=no-1
        DisplayPattern(no)


def main():
    no = int(input("Enter the Number: "))
    DisplayPattern(no)

if __name__=="__main__":
    main()