class Student:

    school="Saveetha EC"   #class attribute or variable
    @classmethod           #decorator to classify instance methods and class methods
    def getschoolname(cls):         #Class method
        return cls.school


   
    def __init__(self,m1,m2,m3):   #Instance method 
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def avg(self):
        return (self.mark1+self.mark2+self.mark3)/3

    #Accessors
    def get_m1(self):
        return self.mark1
    def set_m1(self,value):
        self.mark1=value
    
    @staticmethod
    def information():
        print("this is static method")
    

s1=Student(2,3,4)  #creating instance objects
s2=Student(6,9,7)

print(s1.avg())    #calling and printing avg method
print(s2.avg())


print(s1.get_m1()) #getting method Accessor

s2.set_m1(5)       #Setting method  Mutator
print(s2.mark1)

print(Student.getschoolname()) #printing class method 
Student.information()      #invoking static method