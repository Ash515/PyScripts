def fact(num):
    factorial=1
    if num>=1:
        for i in range(1,num+1):   # my i values is between 1 to 5
            factorial=factorial*i  #
    print("Factorial is",factorial)
fact(5)
