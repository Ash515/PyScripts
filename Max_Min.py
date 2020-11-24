print("To print the maximum and Minimum values in the list")
def Max(array):
    print("*****Maximum Values******")
    if(array):
        array.sort()
        print("Your sorted list",array)
        Max=max(array)
        return Max
    else:
        return 0
def Min(array):
    print("*****Minimum Values******")
    if(array):
        array.sort()
        print("Your sorted list",array)
        Min=min(array)
        return Min
    else:
        return 0
ary=[]
total=int(input("Enter the total values into list:"))
for i in range(total):
    values=int(input("Enter the list of values:"))
    ary.append(values)
print("The Maximum value in your list is",Max(ary))
print("The Minimum value in your list is",Min(ary))
