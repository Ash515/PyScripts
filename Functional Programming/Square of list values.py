print("To print the square values of your list")
def square_list(List):
    lst=[]
    for i in list:
        lst.append(i**2)
    return lst
    
list=[]

total=int(input("Enter total number of values:"))
for j in range(total):
    values=int(input("Enter the values:"))
    list.append(values)
    list.sort()
print("Your List is",list)
print("Square values of your list is ",square_list(list))
