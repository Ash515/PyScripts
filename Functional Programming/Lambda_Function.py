from functools import reduce
num=[2,3,4,5,6,7,8,9]
even=list(filter(lambda n:n%2==0,num))

print(even)
doubles=list(map(lambda n:n+1,even))
print(doubles)
red=list(reduce(lambda n:n,doubles))
print(red)
