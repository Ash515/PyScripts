print("To Swap a given numbers")
def Two(a,b):
    a,b=b,a
    return a,b
def Three(x,y,z):
    x,y,z=z,y,x
    return x,y,z
print("1.Two Numbers 2.Three Numbers 3.Exit")
choice=int(input("Enter your choice:"))
if (choice==1):
    val1=int(input("Enter the first value:"))
    val2=int(input("Enter the second value:"))
    print("Swapping between two values is:",Two(val1,val2))
elif(choice==2):
     val1=int(input("Enter the first value:"))
     val2=int(input("Enter the second value:"))
     val3=int(input("Enter the third value:"))
     print("Swapping between two values is:",Three(val1,val2,val3))
else:
    exit(0)



