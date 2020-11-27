a=10 #Normal initialization of object to variable a
def global_var():
    global a #declaring that a variable as a global variable here to access or use that a here
    a=a+1 # calculation 
    print(a)
global_var() #calling the function 

"""
output become 11
"""
