print("To print decimal to binary")
n=int(input("Enter the value:"))
pos=1
bin=0
while n!=0:
    rem=n%2
    bin=bin+rem*pos
    n=n//2
    pos=pos*10
print("Answer:",bin)

# or we can directly do bin(n) which give the answer

