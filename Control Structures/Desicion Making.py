print("To print the grade for the marks")
n=int(input("Enter the total number of subjects :"))
for i in range(n):
    mark=int(input("Enter mark:"))
    if(mark>91)and(mark<=100):
        print("Congratulations!!! your grade is S")
    elif(mark>81)and(mark<=90):
        print("Congratulations!!! your grade is A")
    elif(mark>71)and(mark<=80):
        print("Congratulations!!! your grade is B")
    elif(mark>61)and(mark<=70):
        print("Congratulations!!! your grade is C")
    elif(mark>51)and(mark<=60):
        print("Congratulations!!! your grade is D")
    elif(mark>0)and(mark<=50):
        print("Your are fail and your grade is E")
