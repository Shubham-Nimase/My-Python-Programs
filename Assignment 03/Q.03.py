# Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5
def ListMin(List):

    Min=List[0]
    for i in range(len(List)):
        if List[i]<Min:
            Min=List[i]
    return Min

def main():
    List=list()
    ListSize=int(input("Enter the number of elements: "))

    for i in range(ListSize):
        no=int(input("No. :"))
        List.append(no)

    print("Your Data: ",List)
    print("Minimum number from that list is:",ListMin(List))

if __name__=="__main__":
    main()