class avengers:
    def __init__(self,name,age,gender,superpower,weapon):
        self.name=name
        self.age=age
        self.gender=gender
        self.superpower=superpower
        self.weapon=weapon
    def display(self):
        print('name='+self.name)
        print('age='+str(self.age))
        print('gender='+self.gender)
        print('super power='+self.superpower)
        print('weapon='+self.weapon)
    def is_leader(self,avengers):
        if avengers.index(self)==0:
            return True
        else:
            return False
 
         


captian_america=avengers('captian_america',52,'male','super strenght','shield')
captian_america.display()
ironman=avengers('ironman',35,'male','technology','armor')
ironman.display()
black_widow=avengers('black_widow',32,'female','super human','batons')
black_widow.display()
hulk=avengers('hulk',40,'male','unlimited strenght','no weaspone')
hulk.display()
thor=avengers('thor',30,'male','super energy','mojlnir')
thor.display()
hawkeye=avengers('hawkeye',30,'male','fighting skills','bow and arrow')
hawkeye.display()
avengers=[hulk,ironman,black_widow,captian_america,thor,hawkeye]
for avenger in avengers:
    if avenger.is_leader(avengers):
        print(avenger.name + " is a leader.")
    else:
        print(avenger.name + " is not a leader.")