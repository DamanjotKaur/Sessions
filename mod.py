# # Ass1
# import datetime
# x=datetime.datetime.now()
# print(x)
#
# # Ass2
# class b():
#     __a=20
#     def f1(self):
#         print(self.__a)
#     def __f2(self):
#         print("hello")
#     def f3(self):
#         self.__f2()
# h=b()
# h.f1()
# h.f3()
#
# # Ass3
# class a():
#     __a="name"
#     __b="rollno"
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def setname(self,a):
#         self.__a=a
#     def getname(self):
#         return self.__a
#     def setname(self,b):
#         self.__b=b
#     def getname(self):
#         return self.__b
# obj=a('daman',5)
# obj.setname('daman')
# print(obj.getname())
# obj.setname(5)
# print(obj.getname())
#
# # Ass4
# from abc import ABC,abstractmethod
# class a(ABC):
#     def f1(self):
#         print("hello")
#         @abstractmethod
#         def f2(self):
#             pass
# class b(a):
#     def f2(self):
#         print("world")
# ob=b()
# ob.f1()
# ob.f2()

# Ass5
from abc import ABC,abstractmehtod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")
a=human()
a.move()
b=snake()
b.move()
c=dog()
c.move()
d=lion()
d.move()



