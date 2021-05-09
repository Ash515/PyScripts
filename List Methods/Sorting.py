print("To sort a list ")
a=[]
size=int(input("size:"))
for i in range(size):
    values=int(input("Enter the values: "))
    a.append(values)
a.sort()
print("Your sorted list is",a)
