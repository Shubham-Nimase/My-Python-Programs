# Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def ListNumFreq(List,Search):
    freq=0

    for i in range(len(List)):
        if List[i]==Search:
            freq=freq+1
    return freq

def main():
    List=list()
    ListSize=int(input("Enter the number of elements: "))

    for i in range(ListSize):
        no=int(input("NO. :"))
        List.append(no)
    print("Your Data is: ",List)

    Search=int(input("Enter the searching number: "))

    print("Frequncy of {} number is {}.".format(Search,ListNumFreq(List,Search)))
if __name__=="__main__":
    main()