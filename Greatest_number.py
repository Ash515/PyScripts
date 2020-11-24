print("To print a greatest value among given 3 values")
val1=int(input("Enter the 1st value :"))
val2=int(input("Enter the 2st value :"))
val3=int(input("Enter the 3st value :"))
if (val1>val2) and (val1>val3):
    print("The value is :",val1)
elif(val2>val1)and(val2>val3):
    print("The value is :",val2)
else:
    print("The value is :",val3)
