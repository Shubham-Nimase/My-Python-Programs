# Write a recursive program which display below pattern.
# Input : 5
# Output : 1 2 3 4 5

i=1
def DisplayPattern(no):
   global i
   if i<=no:
       print(i,end="  ")
       i=i+1
       DisplayPattern(no)

def main():
    no=int(input("Enter the NUmber: "))
    DisplayPattern(no)

if __name__=="__main__":
    main()