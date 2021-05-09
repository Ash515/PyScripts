'''

Blue Print

class A:
    def f1(self):
        print("F1 is working")
    def f2(self):
        print("F2 is working")

class B(A):  #inheriting A to B
    def f3(self):
        print("F3 is working")
    def f4(self):
        print("F4 is working")

a1=A()
a1.f1()
a1.f2()


b1=B()
b1.f1()
b1.f4()  #calling inherit method from A f4
'''

class Student():
  
    def display(self,dept,regno):
        print("Department:",dept)
        print("Register Number:",regno)

    def fees(self,amount):
        print("Tution Fees: ",amount)
        return amount

class Library(Student):
    
    def __init__(self,fine):
        self.fine=fine
         
    def calc(self,fees,fine):
        total=fees+fine
        print("The total amount:",total)
        return total
    
    def displaylib(self,bookname,fine):
        print("Bookname",bookname)
        print("Fine Amount",fine)
    

s1=Student()

library=Library(200)
library.display("IT",5005)
library.displaylib("Novel",500)
library.calc(s1.fees(100),500)








