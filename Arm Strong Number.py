print("To check wheather the given number is arm strong or not ")
n=int(input("Enter the 3 digt values:"))
val=[int(d) for d in str(n)]
#val=[1,5,3]
c=0
l=[]
for i in val:
    c=i**3
   
    l.append(c)
a=0
for i in l:
    a=a+i


if(a==n):
    print("It is an Arm strong ")
else:
    print("not an arm strong")



    
