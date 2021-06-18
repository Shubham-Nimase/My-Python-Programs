# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
#
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204


def filter(List):
    List2=[]
    for i in range(len(List)):
        if List[i]%2==0:
            List2.append(List[i])
    return List2

def map(List2):
    for i in range(len(List2)):
        List2[i]=List2[i]*List2[i]
    return List2

def reduce(List):
    Add=0
    for i in range(len(List)):
        Add=Add+List[i]
    return Add

def main():
    List=[]
    ListSize=int(input("ENter the number of elements: "))

    for i in range(ListSize):
        no=int(input("No. :"))
        List.append(no)
    print("Your Data: ",List)

    ret=filter(List)
    print("List After Filter: ",ret)

    ret1=map(ret)
    print("List After Map: ",ret1)

    ret2=reduce(ret1)
    print("List After Reduce: ",ret2)

if __name__=="__main__":
    main()

#///////////////////////////////////////////////////////////////////////////////////////////////////
#
# from functools import reduce
#
# def main():
#     print("Enter The Element")
#     size = int(input())
#     arr = []
#     for i in range(size):
#         print("Enter {} Number".format(i + 1))
#         arr.append(int(input()))
#
#     output = reduce(lambda no1,no2 : (no1 + no2),list(map(lambda no : no * no , list(filter(lambda no : no % 2 == 0,arr)))))
#
#     print(output)
#
# if __name__ == "__main__":
#     main()