print("To check wheather the given number is arm strong or not ")
num=int(input("Enter the number:"))
temp=num
sum=0
while temp!=0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print("The given {} number is palindrome".format(num))
else:
    print("The given {} number is not a palindrome".format(num))
