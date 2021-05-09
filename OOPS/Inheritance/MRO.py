'''
Contructor in inheritance
'''
class A:
    def __init__(self):
        print("A init")
    def f1(self):
        print("F1 is working")
    def f2(self):
        print("F2 is working")

class B(A): 
    
    def __init__(self):
        super().__init__()
        print("B init")
  
    def f3(self):
        print("F3 is working")
    def f4(self):
        print("F4 is working")
class C(B):
     def __init__(self):
        super().__init__()
        print("C init")
     def f5(self):
        print("F5 is working")
     def f6(self):
        print("F6 is working")
    
     def feet(self):
         super().f4()   #method inheriting




b1=C()
b1.feet()
