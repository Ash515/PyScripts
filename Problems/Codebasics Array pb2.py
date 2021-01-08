'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''
Heros=['spider man','thor','hulk','iron man','captain america']
#01 solution
print(len(Heros))
#02 solution
p=Heros.append('black panther')
print(Heros)
#03 solution
a=Heros.remove(Heros[5])
b=Heros.insert(3,'black panther')
print(Heros)
#04 solution
c=Heros.remove(Heros[3])
d=Heros.remove(Heros[4])
e=Heros.insert(3,'strange')
print(Heros)
#05 solution
h=Heros.sort()
print(Heros)

