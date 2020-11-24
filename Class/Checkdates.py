import Date
print("To check the individuall is eligible based upon their age")
def main():
    bornbefore=Date(20,5,2000)
    dat=prompt()
    while dat is not None:
        if (dat<=bornbefore):
            print("You are eligible")



def prompt():
    month=(int(input("enter month or enter 0 to quit")))
    if (month==0):
        return None
    else:
        day=int(input("Enter date:"))
        year=int (input("Enter the year "))
        return Date(month,day,year)

