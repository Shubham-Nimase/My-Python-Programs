# Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def ListAdd(List):
    sum=0
    for i in range(len(List)):
        sum=sum+List[i]
    return sum

def main():
    List=[]
    size=int(input("Enter the number of elements:"))

    for i in range(size):
        print("Enter",i+1,"number Element")
        no=int(input())
        List.append(no)
    print("Your List is:",List)

    print("Addition of List elements is:",ListAdd(List))
if __name__=="__main__":
    main()