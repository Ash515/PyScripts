name="asowin"
new_names=list(name)
vowel="aeiou"
new_vowels=list(vowel)
res=[]
for i in new_names:
    for j in new_vowels:
        if(i==j):
            res.append(i)
print(res)   #['a', 'o', 'i']
          
        

    
       
