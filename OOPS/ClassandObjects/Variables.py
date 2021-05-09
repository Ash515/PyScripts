class Bird:
    features=2  #Static or class variables
    def __init__(self):  #Instance variables
        self.name="crow"
        self.legs=2
    
    def printing(self):
        print("Name =",self.name,"Legs =",self.legs)


b1=Bird()
b2=Bird()

b2.name="Parrot"
b1.legs=3

b1.printing()
b2.printing()
print("Features of b1",b1.features)
print("Features of b2",b2.features)

