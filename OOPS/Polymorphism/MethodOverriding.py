class Father:
    
    def show(self,a,b):
        print("Main")
        c=a+b
        print(c)
        return c


class Son(Father):
  
       def show(self,a,b):
        print("Subclass")
        c=a+b
        print(c)
        return c #overrides here


myphone=Son()
myphone.show(85,36)