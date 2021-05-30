#
#
#
#
# class Base:
#     def __init__(self):
#         self.no1 = 11           #public member
#         self._no2 = 21          #protected member
#         self.__no3 = 51         #private member
#
#     def fun(self):                                  #public method
#         print(self.no1, self._no2, self.__no3)
#
#     def _fun(self):                                 #Protected method
#         print("1")
#         print(self.no1,self._no2,self.__no3)
#
#     def __fun(self):                                #private method
#         print(self.no1,self._no2,self.__no3)
#
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#
#     def gun(self):
#         print(self.no1)
#         print(self._no2)
#         # print(self.__no3)
#
# def main():
#     bobj = Base()
#
#     print(bobj.no1)
#     print(bobj._no2)
#     # print(bobj.__no2)
#
#     bobj.fun()
#     bobj._fun()
#     # bobj.__fun()
#
#     dobj = Derived()
#     dobj.gun()
#
#
# if __name__=="__main__":
#     main()


#///////////////////////////////////////////////////////////////////////////////////////////////////////////


#
# class Demo:
#     def __init__(self):
#         self.public = 10
#         self._protected = 20
#         self.__private = 30
#
#     def publicfun(self):
#         print("Public Fun")
#
#     def _protectedfun(self):
#         print("Protected Fun")
#
#     def __privatefun(self):
#         print("Private Fun")
#
#
# obj = Demo()
# print(obj.public)
# print(obj._protected)
# # print(obj.__private)
#
# obj.publicfun()
# obj._protectedfun()
# # obj.__privatefun()
#

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

# class Base:
#     def __init__(self):
#         self.i = 10
#         self.j = 20
#
#     def fun(self):
#         print("Base fun")
#
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         #self.__init__()        Recursive Call
#         #super().__init__()
#
#         self.x = 30
#         self.y = 40
#
#
#
#     def gun(self):
#         print("Derived gun")
#         Base.fun(self)
#         self.fun()
#         super.fun()
#
#         #print(i)
#
#         print(self. i)
#         print(super().i)
#
#
# dobj = Derived()
# dobj.gun()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# class Base:
#     def __init__(self):
#         self.i = 10
#
#     def fun(self):
#         print("Base fun")
#
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         self.i=20
#         # self.__init__()        Recursive Call
#         # super().__init__()
#
#     def gun(self):
#         print("Derived gun")
#         self.fun()
#         super().fun()
#         print(Base().i)
#         print(self.i)
#         # print(i)
#
# dobj = Derived()
# dobj.gun()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

#
# class Demo:
#     # def Add(self,no1,no2):
#     #     return no1+no2
#     #
#     # def Add(self, no1, no2, no3):
#     #     return no1 + no2 + no3
#
#     def Add(self,no1 = None,no2 = None,no3 = None):
#
#         if no1 != None and no2 != None and no3 != None:
#             return no1+no2+no3
#         elif no1 != None and no2 != None:
#             return no1+no2
#         elif no1 != None:
#             return no1
#         else:
#             return 0
#
#
# obj = Demo()
#
# ret = obj.Add(10,20,30)
# print(ret)
#
# ret = obj.Add(10,20)
# print(ret)
#
# ret = obj.Add(10)
# print(ret)
#
# ret = obj.Add()
# print(ret)
#

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

class C:
    def LearnAndCode(self):
        print("Learning C programming...")

class CPP:
    def LearnAndCode(self):
        print("Learning C++ programming...")

class Golang:
    def LearnAndCode(self):
        print("Learning Golang programming...")

class Demo:
    pass


class Programmer:
    def Coding(self,language):
        language.LearnAndCode()


cobj = C()
cpobj = CPP()
gobj = Golang()

dobj = Demo()

obj = Programmer()

obj.Coding(cobj)
obj.Coding(cpobj)
obj.Coding(gobj)
#obj.Coding(dobj)









