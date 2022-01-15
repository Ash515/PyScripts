a=int(input("Value:"))
b=int(input("value"))
i=1
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        gcd=i
    i=i+1
print("GCD is",gcd)
