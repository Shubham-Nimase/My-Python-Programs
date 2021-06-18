# Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List.
# Main python file accepts N numbers from user and pass each number to ChkPrime() function
# which is part of our user defined module named as MarvellousNum.
# Name of the function from main python file should be ListPrime().

# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)


import MarvellousNum as MN

def main():
    List=[]
    ListSize=int(input("Enter the number of elements: "))

    for i in range(ListSize):
        no=int(input("nos. :"))
        List.append(no)
    print("Your Data: ",List)

    ret=MN.ChkPrime(List)
    print("Addition of prime number is: ",ret)

if __name__=="__main__":
    main()

