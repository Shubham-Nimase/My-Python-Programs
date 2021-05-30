#
#
# class Demo:
#     x = 10      #class Variable
#     y = 20        #class Variable
#     def __init__(self):
#         print("Inside Constructor")
#         self.i = 30     #Instance variable
#         self.j = 40     #Instance variable
#
#     def __del__(self):
#         print("Inside Destructor")
#
#     def fun(self):
#         print("Inside fun")
#
# def main():
#     obj1 = Demo()
#     obj2 = Demo()
#
#     obj1.fun()
#     obj2.fun()
#
#     del obj1
#     del obj2
#
#     obj2.fun()
#
#
# if __name__ == "__main__" :
#     main()
#
#
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
# Design object oriented python application which accept N numbers from user and perform below opration
#
# Display all even numbers
# calculate the summation of all numbers
# Display all perfect numbers


class Numbers:

    def __init__(self,no=10):
        self.size = no
        self.arr = []

    def Accept(self):
        print("Please Enter the Elements: ")

        for i in range(self.size):
            print("Enter Number :",i+1)
            no = int(input())
            self.arr.append(no)

    def Display(self):
        print("Elements of list are: ")

        for i in range(self.size):
            print(self.arr[i])

    def Summation(self):
        sum = 0

        for i in range(self.size):
            sum= sum+self.arr[i]
        return sum

    def EvenDisplay(self):
        print("Even elements from List are : ")

        for i in range(self.size):
            if(self.arr[i]%2) == 0:
                print(self.arr[i])

    def PerfectDisplay(self):
        sum = 0
        print("Perfect Numbers are:")
        for i in range(self.size):
            for j in range(1,int(self.arr[i]/2)+1):
                if(self.arr[i] % j) == 0:
                    sum = sum+j
            if sum == self.arr[i]:
                print(self.arr[i])
            sum = 0

    def PrimeDisplay(self):
        flag = False
        print("Prime Numbers are : ")
        for i in range(self.size):
            for j in range(2,int(self.arr[i]/2)+1):
                if(self.arr[i] % j) == 0:
                    flag = True
                    break
            if flag == False:
                print(self.arr[i])
            flag = False


def main():

    value = int(input("Enter the number of elements :"))

    obj1 = Numbers(value)
    obj1.Accept()
    obj1.Display()

    ret = obj1.Summation()
    print("Summation of all Elements : ",ret)

    obj1.EvenDisplay()

    obj1.PerfectDisplay()

    obj1.PrimeDisplay()

if __name__ == "__main__":
    main()
