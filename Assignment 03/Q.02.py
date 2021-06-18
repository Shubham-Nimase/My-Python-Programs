# Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56
def ListMax(arr):
    Max=0
    for i in range(len(arr)):
        if arr[i]>Max:
            Max=arr[i]
    return Max

def main():
    #List=[]
    arr=list()

    ListSize=int(input("Enter the number of Elment:"))

    for i in range(ListSize):
        no=int(input("number:"))
        arr.append(no)
    print("Your data is:",arr)

    print("Maximum number from list is: ",ListMax(arr))

if __name__=="__main__":
    main()