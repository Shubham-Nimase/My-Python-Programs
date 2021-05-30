
# #recursive Function
#
# def DisplayIF(no):
#
#     for i in range(no):             #Iterative Function of for loop
#         print("Hello F")
#
#
# def DisplayIW(no):                  #Iterative Fnnction of While loop
#     while no != 0:
#         no = no - 1
#         print("Hello W")
#
#
# def DisplayR(no):                   #recursive Function==Calling the function from same functiom
#     if no!=0:
#         no=no-1
#         print("Hello R")
#         DisplayR(no)
#
#
# def main():
#     print("Enter the number of iterations :")
#     value=int(input())
#
#     print("Calling the for loop Function: ")
#     DisplayIF(value)
#
#     print("Calling the while loop Function: ")
#     DisplayIW(value)
#
#     print("Calling the Recursive Function: ")
#     DisplayR(value)
#
# if __name__=="__main__":
#     main()
#
#

#-------------------------------------------------------------------------------------------------------


#
# i = 1           #Define the variable
#
# def fun():
#     global i    #declare the variable
#     print(i)
#     i=i+1
#     fun()
#
#
# def main():
#     fun()
#
# if __name__=="__main__":
#     main()

# -------------------------------------------------------------------------------------------------------

#
# import sys
#
# def main():
#     print("Recursion Limit:",sys.getrecursionlimit())
#     sys.setrecursionlimit(1500)
#     print("Recursion Limit:",sys.getrecursionlimit())
#
# if __name__=="__main__":
#     main()

# -------------------------------------------------------------------------------------------------------
def AdditionF(data):
    sum=0
    for i in range(len(data)):sum=sum+data[i]
    return sum

def AdditionW(data):
    sum=0
    i=0

    while i<len(data):
        sum=sum+data[i]
        i=i+1
    return sum

sum=0
i=0

def AdditionR(data):
    global sum
    global i

    if i < len(data):
        sum=sum+data[i]
        i=i+1
        AdditionR(data)
    return sum





def main():
    list=[]
    print("Enter the size of list: ")
    size=int(input())

    for i in range(size):
        print("Enter the Element of list: ")
        list.append(int(input()))
    print("Your List:",list)

    print("Addition of list is:",AdditionF(list))
    print("Addition of list is:",AdditionW(list))
    print("Addition of Recursion list is:",AdditionR(list))

if __name__=="__main__":
    main()
