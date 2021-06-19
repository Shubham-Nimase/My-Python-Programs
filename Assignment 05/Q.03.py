# Write a recursive program which display below pattern.
# Input : 5
# Output : 5 4 3 2 1
#

def DisplayPattern(no):
    if no>0:
        print(no,end=" ")
        no=no-1
        DisplayPattern(no)

def main():
    print("ENter the number: ")
    no=int(input())

    DisplayPattern(no)
if __name__=="__main__":
    main()