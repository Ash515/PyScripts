class A:
    def f1(self):
        print("F1 is working")
    def f2(self):
        print("F2 is working")

class B(A):  #inheriting A to B singl level
    def f3(self):
        print("F3 is working")
    def f4(self):
        print("F4 is working")

class C(B):  #Multilevel Inheriatance 
     def f5(self):
        print("F5 is working")


a1=A()
b1=B()
c1=C()

c1.f5()  #Inherits from A->B->C
c1.f3()
c1.f2()
c1.f1()
c1.f4()


    