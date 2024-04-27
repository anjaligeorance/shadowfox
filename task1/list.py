justice_league=["superman","batman","wonder women","flash","aquaman","green lantern"]
count=len(justice_league)
#1.list
#q1
print("count in list justice_leaque="+str(count))
#q2
justice_league.append('batgirl')
justice_league.append('nightwing')
print(justice_league)
#q3
justice_league.remove("wonder women")
justice_league.insert(0,"wonder women")
print(justice_league)
#q4
justice_league.remove("superman")
iaquaman=justice_league.index("aquaman")
iflash=justice_league.index("flash")
igreen_lantern=justice_league.index("green lantern")
if iaquaman>iflash :
   justice_league.insert(iaquaman,"superman")
else :
   justice_league.insert(iflash_lantern,"superman")
print(justice_league)
#q5
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)
#q6
justice_league.sort()
justice_league.insert(0,'hero')
print(justice_league)

