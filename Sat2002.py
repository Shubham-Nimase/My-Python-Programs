#
# def Addition(no1,no2):
#     return no1+no2
#
# def Main():
#     print("Enter first Number")
#     value1=int(input())
#
#     print("Enter Second Number")
#     value2 = int(input())
#
#     ret=Addition(value1,value2)
#     print("Addition is : ",ret)
#
# if __name__=="__main__":
#     Main()
#
#
#=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/
#
# #Named Function
#
# def Addition(no1,no2):
#     return no1+no2
#
# #Lambda Function
#
# sum=lambda no1,no2:no1+no2
#
#
# def fun(name):
#     ret=name(10,20)
#     print("value from fun is:",ret)
#
# def Main():
#     print("Enter first Number")
#     value1 = int(input())
#
#     print("Enter Second Number")
#     value2 = int(input())
#
#     ret = Addition(value1, value2)
#     print("Addition is : ", ret)
#
#     ret=sum(value1,value2)
#     print("Addition with Lambda :",ret)
#
#     fun(sum)
#
# if __name__=="__main__":
#     Main()

# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/

#Accept N numbers from user and filter out only even numbers from that N numbers
# ...after that add two in evry even numbers
# after the addition of 2 perform summation that modified numbers

#INput=[1,3,2,4,6,5,4]

# after reduce= [2,4,6,4]
# after map= [4,6,8,6]
# after reduce 24

#
# def CheckEven(no):
#     if no%2==0:
#         return True
#     else:
#         return False
#
# # def MarvellousFilter(list1):
# #     list2=[]
# #
# #     for i in range(len(list1)):
# #         if list1[i]%2==0:
# #             list2.append(list1[i])
# #     return  list2
#
# def MarvellousFilter(list1):
#
#     list2=[]
#
#     for i in range(len(list1)):
#         if CheckEven(list1[i])==True:
#             list2.append(list1[i])
#     return list2
#
# def MarvellousMap(list1):
#
#     for i in range(len(list1)):
#         list1[i]=list1[i]+2
#     return list1
#
# def MarvelloudReduce(list1):
#     sum=0
#     for i in range(len(list1)):
#         sum=sum+list1[i]
#     return sum
# ##############################################
#
#
#
# def main():
#
#     list1=[]
#
#     print("Enter the number of elements :")
#     size=int(input())
#
#     for i in range(size):
#         print("Enter the Elements: ",i+1)
#         no=int(input())
#         list1.append(no)
#     print("You Entered data: ",list1)
#
#     EvenData=MarvellousFilter(list1)
#     print("After filtering data is:",EvenData)
#
#     AddEvenData=MarvellousMap(EvenData)
#     print("After map data is:",AddEvenData)
#
#     output=MarvelloudReduce(AddEvenData)
#     print("Final Addition is:",output)
#
# if __name__=="__main__":
#     main()


# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/

import functools

def main():
    arr=[]
    print("Enter the number of element:")
    size=int(input())

    for i in range(size):
        print("Enter the element: ",i+1)
        no=int(input())
        arr.append(no)

    print("Your Entered data is:",arr)

    EvenData = list(filter(lambda No:(No%2==0),arr))
    print("After filtering data is:", EvenData)

    AddEvenData = list(map(lambda No:(No+2),EvenData))
    print("After map data is:", AddEvenData)

    output = functools.reduce(lambda No1,No2:(No1+No2),AddEvenData)
    print("Final Addition is:", output)


if __name__=="__main__":
    main()

# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/











