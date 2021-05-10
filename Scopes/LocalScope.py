'''
variables which can access inside a function defintion 
'''

def calculation():
    a=400
    b=200
    c=a*b
    print(c)
    return c

calculation()

def Student():
    name="Ashwin"
    regno=2005
    def fees():
        a=100
        b=200
        c=200+500
        print("The name of student:",name)
        print("The regno of student:",regno)
        print("The Fees of student:",c)
        return c
    fees()
Student()
