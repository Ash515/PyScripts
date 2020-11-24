print("To validate a given password is valid or not")
def Validate(password):
    special=["!","@","#","$","%",'^',"&","*"]
    val=True
    if (len(password)<8 ):
        print("please enter password size maximum")
        val=False
    elif not any(char.isdigit() for char in password):
        print("Your password not contain numerical value")
        val=False
    elif not any(char.isupper() for char in password):
        print("Your password not contain upper case value")
        val=False
    elif not any(char.islower() for char in password):
        print("Your password not contain lower case value")
        val=False
    if val:
        return val
pwd=input("Enter your password:")

if(Validate(pwd)):
    print("Valid Password !")
else:
    print("Not valid password")

