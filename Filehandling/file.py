from os import write


f = open("demo.txt","a")
content=f.write("and love to code ")
print(content)
f.close()

with open('JavaScript.txt','w') as f:  #create a new file
    lines=["Hi js","\n Love you "]
    f.writelines(lines)

