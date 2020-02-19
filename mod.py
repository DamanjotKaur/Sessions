# Ass1
import datetime
x=datetime.datetime.now()
print(x)

# Ass2
class b():
    __a=20
    def f1(self):
        print(self.__a)
    def __f2(self):
        print("hello")
    def f3(self):
        self.__f2()
h=b()
h.f1()
h.f3()

# Ass3
class a():

    def __init__(self,fname,frollno):
        self.fname=fname
        self.frollno=frollno