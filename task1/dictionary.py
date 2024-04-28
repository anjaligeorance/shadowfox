#q1
friends=['anju','abhijit','minnu','meron','ancy']
ftuple=[('anju',4),('abhijit',6),('minnu',5),('meron',5),('ancy',4)]
#q2
myexpense={
    "travel": 1500,
    "food": 1000,
    "hotel":2000,
    "pub":500,
    "miscellanous":200,
}
partnerexpense={
    "travel": 1000,
    "food": 1200,
    "hotel":2000,
    "pub":200,
    "miscellanous":200,
}
#2a.
my_total=sum(myexpense.values())
partner_total=sum(partnerexpense.values())
print('myexpense='+str(my_total))
print('pertnerexpense='+str(partner_total))
#2b.
if my_total > partner_total:
    print("You spent more money than your partner.")
elif my_total < partner_total:
    print("Your partner spent more money than you.")
else:
    print("You and your partner spent the same amount of money.")
#2c
diff=0;
max_value=0
category='none'
for i in myexpense:
    diff=abs(myexpense[i]-partnerexpense[i])
    
    if diff>max_value:
        max_value=diff
        category=i

print('The category that you and your partner spent the most money on was '+category+'and the difference in amount='+str(max_value))





