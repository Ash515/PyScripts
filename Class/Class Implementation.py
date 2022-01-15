class score:
    def __init__(self,Maths,physics,chemistry):
        self.Maths=Maths
        self.physics=physics
        self.chemistry=chemistry
        
    def result(self):
        total=self.Maths+self.physics+self.chemistry
        print("Your score is",total)


#creating an instance of object by calling class
Ashwin=score(60,30,80)
hari=score(60,80,90)

Ashwin.result()
hari.result()
