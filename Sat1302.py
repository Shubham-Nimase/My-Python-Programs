# import sys
#
# #NUmber : int,float,complex
# # Everything in python is considerd as an object...
#
# print("Jay Ganesh...")
# no=11
# print(no)
# print(id(no))
# print(type(no))
# print(sys.getsizeof(no))
#
# f=11.20
# print(f)
# print(id(f))
# print(type(f))
# print(sys.getsizeof(f))
#
# str="JAy raam "
# print(str)
# print(id(str))
# print(type(str))
# print(sys.getsizeof(str))

#----------------------------------------------------------------------------------------------

#Defination of function
#
# def Addition(no1,no2):
#     ans=no1+no2
#     return ans


#----------------------------------------------------------------------------------------------

# import Arithmatic
#
# def main():
#     print("Enter First Number")
#     value1=int(input())
#
#     print("Enter Second Number")
#     value2 = int(input())
#
#     ret=Arithmatic.Addition(value1,value2)
#     print("Addition of {} and {} is {} ".format(value1,value2,ret))
#     #printf("Addition of %d and %d is %d",value1,value2,ret)
#
#     ret = Arithmatic.Substraction(value1, value2)
#     print("Substraction of {} and {} is {} ".format(value1, value2, ret))
#     # printf("Addition of %d and %d is %d",value1,value2,ret)

#----------------------------------------------------------------------------------------------

#types of function defination

#Accept nothing return nothing
# def fun():
#     print("Inside Fun")
#
# #Accept Parameter return nothing
# def gun(value):
#     print("inside gun",value)
#
# #Accept Parameter return one value
# def sun(value1):
#     value=value1+1
#     print("inside sun")
#     return value
#
# def mun():
#     pass
#
# #Nested FUnction:
#
# def Outer():
#     print("inside Outer")
#     def Inner():
#         print("Inside Inner")
#         Inner()
#
#----------------------------------------------------------------------------------------------
#import sys
# def main():
#     print("NUmber of arguments are : ",len(sys.argv))
#     fun()
#     gun(10)
#     ret=sun(11)
#     print(ret)
#     mun()
#     Outer()
#
#
# if __name__=="__main__":
#     main()

#----------------------------------------------------------------------------------------------
#
# import sys
#
# def Addition(no1,no2):
#     return no1+no2
#
# def main():
#     if len(sys.argv)<3 or len(sys.argv)>3:
#         print("Sorry Boss...Invalid number of Arguments...!!")
#         return
#
#
#     ret=Addition(int(sys.argv[1]),int(sys.argv[2]))
#     print("Addition of {} and {} is {} ".format(sys.argv[1],sys.argv[2],ret))
#
# if __name__=="__main__":
#     main()
#
#----------------------------------------------------------------------------------------------
#types of arguments are:

#Positional ARguments
# def Student(name,rno,address,marks):
#     print("Name is : ",name)
#     print("Roll no is : ",rno)
#     print("Address is : ",address)
#     print("Marks is : ",marks)
#
# #keyword arguments
# def Computer(RAM,Proccesor,HDD):
#     print("RAM Size is : ",RAM)
#     print("Proccsor name is : ",Proccesor)
#     print("Size of HDD : ",HDD)
#
# #default arguments(Should be from right to left)
# def CircleArea(Radius,PI=3.14):
#     print("Value of PI is: ",PI)
#     return PI*Radius*Radius
#
#
# #variable number of arguments
#
# def fun(*value):
#     print("NUmber of arguments are: ",len(value))
#
#
# def main():
#     Student("Shubham","22","Mandava","98")
#
#     Computer(RAM=8,Proccesor="i9",HDD="1T")
#
#     ret1=CircleArea(14)
#     ret=CircleArea(Radius=14,PI=7.12)
#     print("CircleArea is :",ret1)
#     print("CircleArea is :",ret)
#
#     fun()
#     fun(10)
#     fun(10,20,30,40)
#     fun(10,20,30,40,20,2020)
#
# if __name__=="__main__":
#     main()
#----------------------------------------------------------------------------------------------

def Addition(*Arr):
    sum=0
    for i in Arr:
        sum=sum+i
    return sum

def main():
    ret=Addition(10,20,30,40,50)
    print("Addition is :",ret)

    print(type(Addition()))

    ret = Addition(20, 30)
    print("Addition is :", ret)

if __name__ == "__main__":
    main()
#----------------------------------------------------------------------------------------------
#
# import sys
#
# no=4504521140
# b=450452140
# print(type(no))
# print(id(no))
# print(id(b))
#
# print(sys.getsizeof(no))
# print(sys.getsizeof(b))
#----------------------------------------------------------------------------------------------
# def StudentInfo(** Other):
#     print(Other,"\n")
#
#     for i,j in Other.items():
#         print(i,j)
#
#
# def Main():
#     print("\nDemostration of keyword variable number of Arguments :-\n")
#
#     StudentInfo(age=22,Address="Mandava",Mobile=915881252,Company="Ashuro soft pvt.limited...")
#
#
#
# if __name__=="__main__":
#     Main()
#
#----------------------------------------------------------------------------------------------






