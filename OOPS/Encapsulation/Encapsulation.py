


class Car():
    def __init__(self,speed,color):
        self.__speed=speed
        self.color=color
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self,value):
        return self.__speed

    
s1=Car(200,"red")
print(s1.get_speed())
print(s1.__speed)






        
    


