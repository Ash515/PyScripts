print("To print the Simple Interst and Compound Interst")
def SI(P,N,R):
    SimpleInterst=(P*N*R)/100
    return SimpleInterst
def CI(P,R,T):
    Compint=  P* (pow((1 + R / 100),T)) 
    return Compint
print("1.Simple Interest 2.Compound Interst 3.Exit")
choice=int(input("Enter your choice:"))
if(choice==1):
    principle=int(input("Enter the principle amount:"))
    years=int(input("Enter the no of years:"))
    interest=int(input("Enter the interst:"))
    print("Your SI amount is,",SI(principle,years,interest))
elif(choice==2):
    principle=int(input("Enter the principle amount:"))

    interest=int(input("Enter the interst:"))
    time=int(input("Enter the time period:"))
    print("Your Compound interst is,",CI(principle,interest,time))
else:
    exit(0)



