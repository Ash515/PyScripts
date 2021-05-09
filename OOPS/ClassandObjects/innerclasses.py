class student:
    def __init__(self,name,rollno):
        self.name=name
        self.roll=rollno
     
    
    def show(self):
        print(self.name, self.roll)
      
    
    class laptop:   #innerclass
        def __init__(self,ram,cpu):
            self.ram=ram
            self.cpu=cpu
        def print(self):
            print(self.ram,self.cpu)


    


s1=student("Ashwin",23)
s2=student("Hari",25)
s1.show()
s2.show()

#Calling innerclass
s1=student.laptop('i8',45)
s2=student.laptop('i5',89)
s1.print()
s2.print()


