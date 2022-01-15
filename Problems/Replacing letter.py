def deleteing(string,letter):
    for i in string:
        if(i==letter):
            print(i)
            print("your new string is ",string.replace(i,''))
            return 
    print("No letter found in your string ")
deleteing("Ashwin","A")

#output - "shwin"
