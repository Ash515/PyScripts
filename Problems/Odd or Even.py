print("To print the sum odd values")
n=int(input("Enter the total values:"))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
        sum-=i
print(sum)
    
        
