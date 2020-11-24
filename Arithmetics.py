#Addition
def add(a,b,c):
    d=a+b+c
    return d
res_add=add(10,20,30)
print(res_add)

#Subtraction

def sub(a,b,c):
    d=a-b-c
    return d
res_sub=sub(10,20,30)
print("1.Normal result 2.Absolute result")
choice=int(input("Enter your choice:"))
if(choice=="1"):
    print(res_sub)
else:
    print(abs(res_sub))

#Multiplication
def multiply(n,k):
    f=n*k
    return f
res_mul=multiply(10,20)
print(res_mul)

#Division

def division(m,n):
    g=m/n
    return g
res_div=print(division(50,10))
