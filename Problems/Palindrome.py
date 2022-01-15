def palindrome(string):
    reverse=string[::-1]
    if (reverse==string):
        print("It is Palindrome")
    else:
        print("Not a palindrome")
print("To Check your name is a palindrome or not")
Name=input("Enter the name:")
palindrome(Name)
