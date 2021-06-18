# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
#
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62




# def filter(List):
#     List2=[]
#     j=2
#     for i in range(j,len(List)):
#         if List[i]%i!=0:
#             List2.append(List[i])
#     return List2
#
# def map(List2):
#     for i in range(len(List2)):
#         List2[i]=List2[i]*2
#     return List2
#
# def reduce(List):
#     Max=List[0]
#     for i in range(len(List)):
#         if List[i]>Max:
#             Max=List[i]
#     return Max
#
# def main():
#     List=[]
#     ListSize=int(input("ENter the number of elements: "))
#
#     for i in range(ListSize):
#         no=int(input("No. :"))
#         List.append(no)
#     print("Your Data: ",List)
#
#     ret=filter(List)
#     print("List After Filter: ",ret)
#
#     ret1=map(ret)
#     print("List After Map: ",ret1)
#
#     ret2=reduce(ret1)
#     print("List After Reduce: ",ret2)
#
# if __name__=="__main__":
#     main()

#/////////////////////////////////////////////////////////////////////////////////////

from functools import reduce

def chkprime(No):
    ret = True
    j = int(No / 2)
    for i in range(2, (j + 1)):
        if No % i == 0:
            ret = False
            break
    return ret

def main():

    List = []
    print("Enter the NUmber of Elements:")
    size = int(input())

    for i in range(size):
        print("Enter {} Number".format(i + 1))
        List.append(int(input()))

    newdata = list(filter(chkprime, List))
    print("List After Filter", newdata)

    newdata1 = list(map(lambda no: no * 2, newdata))
    print("List After Map", newdata1)

    output = reduce(lambda no1, no2: no1 if no1 > no2 else no2, newdata1)
    print("List After Reduce: ",output)


if __name__ == "__main__":
    main()