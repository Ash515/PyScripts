class Student():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
     
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    def __mul__(self,other):
        m1=self.m1*other.m1
        m2=self.m2*other.m2
        mul=Student(m1,m2)
        return mul
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=self.m1+self.m2
        if (r1>r2):
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1=Student(56,89)
s2=Student(10,39)
s3=Student(10,39)

sk=s1+s2+s3


if s1>s2:
    print("a1 wins")
else:
    print("a2 wins")

print(sk)
