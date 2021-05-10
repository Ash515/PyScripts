class iterator():
    def __iter__(self):
       self.a=1
       return self
    
    def __next__(self):
        x=self.a
        self.a+=1
        return x

s1=iterator()
myiter=iter(s1)
print(next(myiter))
print(next(myiter))
print(next(myiter))

