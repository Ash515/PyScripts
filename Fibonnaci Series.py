print("To print the fibonacci series")
def fibonacci(n):
    a=0
    b=1
    if(n==0):
        print(a)
    elif(n<0):
        print("Print Positive values")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
num=int(input("Enter the Number:"))
fibonacci(num)
