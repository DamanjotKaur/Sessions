# Ass1
class student():
    def std1(self):
        s=input("Enter your Age")
        print("Age is:",s)
    def __init__(self):
        print("m1")
class student1(student):
    def std2(self):
        f=input("Enter your Name")
        print("Name is:",f)
obj=student1()
obj.std2()
obj.std1()

# Ass2
class A():
    a=20
    b=20
    def func(self):
        if self.a>self.b:
            print("a is bigger")
        else:
            print("b is bigger")
class B(A):
    x=10
    y=20
    z=x*y
    def func1(self):
        print("The vaue of z:",self.z)
        print("The value of a is:",super().a)
h1=B()
h1.func1()
h1.func()

# Ass3
class a():
    a=20
    x=50
    def __init__(self):
        print("The value of a",self.a)
class b(a):
    b=20
    def func(self):
        print("The value of b",self.b)
class c(b):
    y=30
    def func1(self):
         print("The value of y",self.y)
         print("The value of x",super().x)
h1=c()
h1.func1()
h1.func()
h1.__init__()

# Ass4
class Parent:
    def func1(self):
        print("this is function 1")
class Parent2:
    def func2(self):
        print("this is function 2")
class Child(Parent, Parent2):
    def func3(self):
        print("this is function 3")
ob = Child()
ob.func1()
ob.func2()
ob.func3()
