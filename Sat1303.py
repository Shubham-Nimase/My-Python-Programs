# inbuilt function from module...
#
# def Substraction(no1,no2):
#     return no1-no2
#
# def main():
#     print("Jay shree ram")
#
#     print("ENter first number: ")
#     value1 = int(input())
#
#     print("ENter Second number: ")
#     value2 = int(input())
#
#     ret = Substraction(value1,value2)
#     print("Substraction is: ",ret)
#
# if __name__=="__main__":
#     main()
#

# /////////////////////////////////////////////////////////////////////////////////////////////////////

# inbuilt function from module...

# def Substraction(no1, no2):
#     print("13")
#
#     return no1 - no2
#
# def SubDecorator(func_name):
#     print("8")
#
#     def Updator(a,b):
#         print("9")
#
#         if a < b :
#           a,b = b,a
#           print("10")
#
#         return func_name(a,b)
#     print("11")
#
#     return Updator
#     print("12")
#
# def main():
#     print("2")
#
#     Sub = SubDecorator(Substraction)
#     print("1")
#
#     print("ENter first number: ")
#     value1 = int(input())
#     print("ENter Second number: ")
#     value2 = int(input())
#
#     print("3")
#
#     ret = Sub(value1,value2)
#     print("4")
#
#     print("Substraction is: ", ret)
#
#     print("5")
#
# if __name__ == "__main__":
#     print("6")
#
#     main()
#     print("7")

# /////////////////////////////////////////////////////////////////////////////////////////////////////

# # Multitasking
# import os
# import multiprocessing
# from time import sleep
#
# def Process1(no):
#
#     print("Process1 is created")
#     print("PID of process1 is: ",os.getpid())
#     print("PID of parant process of process1 is: ",os.getppid())
#     for i in range(no):
#         sleep(1)
#         print("Process-1",i)
#
# def Process2(no):
#
#     print("\nProcess2 is created")
#     print("PID of process2 is: ",os.getpid())
#     print("PID of parant process of process2 is: ",os.getppid())
#     for i in range(no):
#         sleep(1)
#         print("Process-2",i)
#
# def main():
#
#     print("Inside Main Process")
#     print("PID of Main process is: ",os.getpid())
#     print("PID of parant process is",os.getppid(),"\n")
#     value = 5
#
#     p1 = multiprocessing.Process(target = Process1,args = (value,))
#     p2 = multiprocessing.Process(target = Process2,args = (value,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print("\nEnd Main Process")
#
# if __name__=="__main__":
#     main()

#/////////////////////////////////////////////////////////////////////////////////////////////////////

#Multitasking

import os
import threading
from time import sleep

def Process1(no):

    print("Process1 is created")
    print("PID of process1 is: ",os.getpid())
    print("PID of parant process of process1 is: ",os.getppid())
    for i in range(no):
        sleep(1)
        print("Process-1",i)

def Process2(no):

    print("\nProcess2 is created")
    print("PID of process2 is: ",os.getpid())
    print("PID of parant process of process2 is: ",os.getppid())
    for i in range(no):
        sleep(1)
        print("Process-2",i)

def main():

    print("Inside Main Process")
    print("PID of Main process is: ",os.getpid())
    print("PID of parant process is",os.getppid(),"\n")
    value = 5

    p1 = multiprocessing.Process(target = Process1,args = (value,))
    p2 = multiprocessing.Process(target = Process2,args = (value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("\nEnd Main Process")

if __name__=="__main__":
    main()


#/////////////////////////////////////////////////////////////////////////////////////////////////////










