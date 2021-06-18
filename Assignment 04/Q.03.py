# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
#
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000



def filter(List):
    List2=[]
    for i in range(len(List)):
        if List[i]>=70 and List[i]<=90:
            List2.append(List[i])
    return List2

def map(List2):
    for i in range(len(List2)):
        List2[i]=List2[i]+10
    return List2

def reduce(List):
    Multi=1
    if len(List)==0:
        print("There is no such elements after Proccessing...!! ")
        return
    for i in range(len(List)):
        Multi=Multi*List[i]
    return Multi

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