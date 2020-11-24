def pop(val):
    return pop(val)


n=int(input("Enter the total value to be inserted in queue:"))
stack=[]
for i in range(n):
    num=int(input("Enter values to be insert:"))
    stack.append(num)
print(stack)
print("1.POP 2.PUSH 3.Exit")
choice=int(input("Enter your choice:"))
if(choice==1):
    value=int(input("Enter which element you need to delete:"))
    val1=value+1
    stack.pop(val1)
    print(stack)
elif(choice==2):
    value2=int(input("Enter the element to be push:"))
    position=int(input("Position:"))
    stack.insert(position,value2)
    print(stack)
else:
    exit(1)
    

    
