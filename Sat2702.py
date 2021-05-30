#///////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////           OOP              ///////////////////////////////////////////
# class Demo:
#     pass
#
# def main():
#     obj= Demo()
#     print(type(obj))
#
#
# if __name__=="__main__":
#     main()

#///////////////////////////////////////////////////////////////////////////////////////////////////
#
# def Add(no1,no2):
#     return no1+no2;
#
# def Sub(no1,no2):
#     return no1-no2;
#
# def main():
#     no1=int(input("Enter first number: "))
#     no2=int(input("Enter second number: "))
#
#     ret=Add(no1,no2)
#     print("Addtion is :",ret)
#
#     ret = Sub(no1, no2)
#     print("Substraction is :", ret)
#
# if __name__=="__main__":
#     main()

#///////////////////////////////////////////////////////////////////////////////////////////////////

class Arithmatic:                           #class Defination

    value=111                               #class variable

    def __init__(self,i,j):                 #class construcor
        print("Inside COnstructor")
        self.no1=i                          #class instance variable
        self.no2=j                          #Instance variable

    def Add(self):                          #Instance Method
        print(Arithmatic.value)
        return self.no1 + self.no2

    def Sub(self):                          #Instance Method
        return self.no1 - self.no2


def main():

    print("Value is: ",Arithmatic.value)


    obj1 = Arithmatic(21,11)            #__init__(obj1,21,11)
    obj2 = Arithmatic(101,51)           #__init__(obj2,101,51)

    print("value is: ",obj1.value)

    ret=obj1.Add()                      #ret = Add(obj1)
    print("Addition is :",ret)
    ret=obj1.Sub()                      #ret = Sub(obj1)
    print("Substraction is :",ret)

    ret=obj2.Add()                      #ret = Add(obj2)
    print("Addition is :",ret)
    ret=obj2.Sub()                      #ret = Add(obj2)
    print("Substraction is :",ret)

if __name__=="__main__":
    main()
