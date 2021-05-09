class Computer:
    def __init__(self,cpu,ram): #Constructor
        self.cpu=cpu
        self.ram=ram

        

    def config(self):   #Method inside class
        print("The Configuration",self.cpu,self.ram)
        


HP=Computer("Intel",8)   #instances
Dell=Computer("Intel1",10)
print(id(HP))

HP.config()
Dell.config()




