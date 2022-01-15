'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
Expenses=[2200,2350,2600,2190]
#1 solution
ans1=Expenses[1]-Expenses[0]
print(ans1)
#2 solution
ans2=Expenses[0]+Expenses[1]+Expenses[2]
print(ans2)
#3 solution
for i in range(len(Expenses)):
    if(Expenses[i]==2000):
            print(i)
    else:
        pass
    
#04 solution
ans3=Expenses.insert(4,1980)
print(Expenses)
#05 solution
ans4=Expenses[3]-200
print(ans4)

        

