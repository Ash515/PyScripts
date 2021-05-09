print("To print the factorial of given number using recursion")
def factorial(n):
    if(n==0):
        return -1
    else:
        return abs(n*factorial(n-1))
num=int(input("Enter the value:"))
print("The factorial of given number is",factorial(num))

        
