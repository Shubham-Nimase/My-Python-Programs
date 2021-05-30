#Demonstration of program...
#sequence...
# def fun():
#     print("First LIne of Function...")
#     print("Second line of function...")
#
# print("First LIne of Application...")
# fun()
# print("Last Line of Application...")
#
# 7 8 3 4 5 8 9

#---------------------------------------------------------------------------------------------------
#Demonstration of program...
#Selection...

# no=10
# if no % 2==0:
#     print("Number is Even...")
# else:
#     print("NUmber is Not even...")
#
#
# 17 -> 18 19 || 20 21

#---------------------------------------------------------------------------------------------------
#
# import MarvellousNumber as MN
#
# def main():
#     print("Enter any NUmber: ")
#     value=int(input())
#
#     bret=MN.ChkEven(value)
#
#     if bret == True:
#         print("{} Number is Even".format(value))
#     else:
#         print("{} Number is Not Even".format(value))
#
#
#
# if __name__=="__main__":
#     main()

#47 48 35 36 37 39 28 -> 29 30 || 31 32 39 -> 41 42 || 43 44
#---------------------------------------------------------------------------------------------------

# def Start1():
#     print("JAy Ganesh...")
#     print("JAy Ganesh...")
#     print("JAy Ganesh...")
#     print("JAy Ganesh...")
#     print("JAy Ganesh...")
#
# def Start(no):
#     i=0;
#     while(i<no):
#         print("Jay")
#         i=i+1
#
# def Main():
#     print("Enter number of times you want to display massage on screen :")
#     no=int(input())
#     Start(no)
#     #Start1()
#
# if __name__=="__main__":
#     Main()
# else:
#     print("Invalid Module Name")

#---------------------------------------------------------------------------------------------------

def DisplayF(no):

    for i in range(0,no,1):
        print("Jay Ganesh",i)

def DisplayW(no):
    icnt=0;
    while(icnt<no):
        print("JAY")
        icnt=icnt+1

def Main():
   print("ENter the number of itrations : ")
   no=int(input())
   DisplayF(no)
   #DisplayW(no)

if __name__=="__main__":
    Main()
#---------------------------------------------------------------------------------------------------
#
# def Main():
#     Arr= [10,20,30,40,50]
#     Arr[1]=70
#
#     print(Arr)
#     print (Arr[2]+Arr[3])
#
#     Brr=[10,"Shubham",86.80,"MAndava Island"]
#
#     print(Brr)
#     print(Brr[3])
#
#
# if __name__=="__main__":
#     Main()
#---------------------------------------------------------------------------------------------------
#
# def Display(List):
#     icnt=0
#     for icnt in range(len(List)):
#         print(List[icnt])
#
# def Addition(Arr):
#     i=0
#     ans=0
#     print(len(Arr))
#     for i in range(len(Arr)):
#         ans=ans+Arr[i]
#     return ans
#
# def Main():
#     Arr=[10,20,30,40,50]
#     Display(Arr)
#     ret=Addition(Arr)
#     print("Addition is :",ret)
#
# if __name__=="__main__":
#     Main()
#---------------------------------------------------------------------------------------------------
# def Addition(Arr):
#     #i=0
#     SUM=0
#     for i in range(len(Arr)):
#         SUM=SUM+Arr[i]
#     return SUM
#
# def Main():
#     arr=[]
#
#     print("Enter number of Elements: ")
#     no=int(input())
#
#     print("Enter Elements")
#     for i in range(no):
#         Value=int(input())
#         arr.append(Value)
#
#     ret=Addition(arr)
#     print("Addition is :",ret)
#
# if __name__ == "__main__":
#     Main()

#---------------------------------------------------------------------------------------------------















