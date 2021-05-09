print("To print the sum of numbers using recursion")
def calculatatesum(num):
    if(num):
        a=num+calculatatesum(num-1)
        return a
    else:
        return 0
n=int(input("Enter the  Number value:"))
print("The Sum of numbers is,",calculatatesum(n))
