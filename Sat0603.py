# # ///////////////////////////////////////////////////////////////////////////////////////////////////
#
# class Marvellous:
#     value1=11                       #Class/Static VAariable
#
#     def __init__(self,no1,no2):     #Constructor
#         self.i=no1                  #instance variable
#         self.j=no2
#         print("INside Consrtuctor...")
#
#     def __del__(self):              #Destructor
#         print("INside Desrtuctor...")
#
#     def fun(self):                  #instance method
#         print("INside fun...")
#         print("value of j is",self.j)
#
# def main():
#
#     obj1 = Marvellous(11,21)            #creating the object
#     obj2 = Marvellous(51,101)
#
#
#     print("value of i from obj1", obj1.i)           #Acessing instatnce members
#     print("value of i from obj2", obj2.i)
#     print("value of Class member",Marvellous.value1)        #Accessing instance method
#
#     obj1.fun()                                          #Calling Instance method
#     obj2.fun()
#
#     del obj1                                            #Deallocating the memory of Object
#     del obj2
#
# if __name__=="__main__":
#     main()
#
# # ///////////////////////////////////////////////////////////////////////////////////////////////////

#
# class Student:
#     School="Aamdar Kakanchi Shala"             #class variable
#
#     def __init__(self,no1,no2,no3):
#         self.m1 = no1
#         self.m2 = no2                   #Instance variable
#         self.m3 = no3
#
#     def Instance_Total(self):           #Instance method
#         print("INside instance Method")
#         return self.m1+self.m2+self.m3
#
#
#     @classmethod                               #Decorator
#     def Class_DisplaySchool(cls):           #Class Method
#         print("School name is: ",cls.School)
#
#     @staticmethod                               #Decorator
#     def Static_Info():                      #class Method
#         print("This class contains the information of school")
#
#
#
#
# def main():
#
#     Student.Class_DisplaySchool()           #Calling class method
#
#     Student.Static_Info()                   #Calling static method
#
#     obj1 = Student(50,80,70)                #object creation
#     obj1 = Student(65,80,75)
#
#     ret = obj1.Instance_Total()             #calling instance method
#     print("Total Obtained Marks: ",ret)
#
# if __name__=="__main__":                    #application starter
#     main()
#
# # ///////////////////////////////////////////////////////////////////////////////////////////////////

# class Base:
#     def __init__(self):
#         self.i=10
#         self.j=20
#         print("INside Base Constructor")
#
#     def fun(self):
#         print("INside Base fun")
#
#     def gun(self):
#         print("INside Base gun")
#
# class Derived(Base):
#
#     def __init__(self):
#         Base.__init__(self)
#
#         self.x=30
#         self.y=40
#         print("INside Derived Constructor")
#
#     def sun(self):
#         print("INside Derived Sun")
#
#     def gun(self):
#         print("INside Derived gun")
#
#
# def main():
#
#     bobj=Base()
#
#     print(bobj.i)
#     print(bobj.j)
#
#     bobj.fun()
#     bobj.gun()
#
#     dobj=Derived()
#
#     print(dobj.i)
#     print(dobj.j)
#
#     print(dobj.x)
#     print(dobj.y)
#
#     dobj.sun()
#     dobj.gun()
#
# if __name__=="__main__":                    #application starter
#      main()
#
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
#     class Base:
#         def __init__(self):
#
#             self.i=10
#             self.j=20
#             print("INside Base Constructor")
#
#     class Derived1(Base):
#
#         def __init__(self):
#             Base.__init__(self)
#
#             self.x=30
#             self.y=40
#             print("INside Derived1 Constructor")
#
#     class Derived2(Derived1):
#
#         def __init__(self):
#             Derived1.__init__(self)
#
#             self.a=50
#             self.b=60
#             print("INside Derived2 Constructor")
#
#     def main():
#
#         dobj=Derived2()
#
#         print(dobj.i)
#         print(dobj.j)
#         print(dobj.x)
#         print(dobj.y)
#
#         print(dobj.a)
#         print(dobj.b)
#
#     if __name__=="__main__":                    #application starter
#          main()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

class Base1:
    def __init__(self):
        self.i = 10
        self.j = 20
        print("INside Base1 Constructor")

    def fun(self):
        print("Base1 fun")

class Base2:
    def __init__(self):
        self.p = 30
        self.r = 40
        print("INside Base2 Constructor")

    def fun(self):
        print("Base2 fun")

class Derived(Base1,Base2):

    def __init__(self):
        Base2.__init__(self)
        Base1.__init__(self)

        self.x = 50
        self.y = 60
        print("INside Derived Constructor")


def main():
    dobj = Derived()

    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)


    print(dobj.p)
    print(dobj.r)

    dobj.fun()

if __name__ == "__main__":  # application starter
    main()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
