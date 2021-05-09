class Books:
    def __init__(self):
        self.cost=250
        self.author="Ram"

    def variety(self):
        print("maths cost =",self.cost,"author =",self.author)
    
    def update(self):
       print("HI ji")
    
    def compare(self,other):
        if self.cost==other.cost:
            return True
        else:
            return False



book1=Books()
book2=Books()

book1.cost=100
book1.author="Ravi"




book1.variety()
book2.variety() 

book1.update()

if book1.compare(book2):
    print("Same ages")
else:
    print("Different values")
    



