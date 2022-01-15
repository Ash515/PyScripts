def lcm(x,y):
    if(x>y):
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0)and(greater%y==0):
            lcm=greater
            break
        greater=greater+1
    return lcm
print("LCm of Values",lcm(54,24))
