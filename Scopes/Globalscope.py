
name="Ashwin"
def student():
    print("Name",name)  #accessing in def also

student()
if name[0]=="A": #accessing in global
        print("Starts from A")


x = 300
def myfunc():
  global x
  x = 200
print(x)
myfunc()

print(x)