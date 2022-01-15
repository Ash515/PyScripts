a=10 #Normal initialization of object to variable a
def global_var():
    global a #declaring that a variable as a global variable here to access or use that a here
    a=a+1 # calculation 
    print(a)
global_var() #calling the function 

"""
output become 11
"""
"""
Global variables for Nested functions
"""
def func_out():
    x=10
def func_in():
    global x
    x=20
    print(x)
func_in()


"""
output 20
Because here we already declare x=10 to func_out() so there is no need to make that x as global in 
func_in().
"""
#globals()

t= 100
def func():
    list_of_items = globals()
    list_of_items["t"] = 15
    t = 22
    print("Local value of t is:", t)
    print("The value of t is:", t)
func()
print("Change in the value of t is:", t)

