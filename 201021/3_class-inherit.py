# Previous class lesson without print text
class Mob:
    def __init__(self, name, health = 10, attack_power = 2):
        self.name = name
        self.health = health
        self.attack_power = attack_power 

    def get_hit(self, power):
        self.health = self.health - power            

    def attack(self, enemy):           
        enemy.get_hit(self.attack_power)
  
#not very useful but valid
class Hero(Mob):#Hero class is a sublclass of Mob
    pass
  
hero = Hero("Sir Galahand")
print(hero.name)

