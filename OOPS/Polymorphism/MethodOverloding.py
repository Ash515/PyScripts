class Student():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def sum(self,a=None,b=None,c=None):
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif (a!=None and b!=None):
             s=a+b
        else:
             s=c
        return s

s1=Student(50,30)
print(s1.sum(20,30))
print(s1.sum(20,30,10))
print(s1.sum(20))
