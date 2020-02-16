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

