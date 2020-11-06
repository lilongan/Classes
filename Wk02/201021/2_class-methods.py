# class Mob:
#     def __init__(self,name,health = 10):
#         self.name = name
#         self.health = health

#     def get_hit(self,power):
#         print(f"I, {self.name}, was hit for {power} points!")

# hero = Mob("Sir Barksalot",30)
# hero.get_hit(6)
# print(hero.health)
# -- -- -- 
class Mob:
    def __init__(self,name,health=10,power=2):
        # Can be substituted with dictionary
        # hero = Mob({
        # health = 10
        # power = 2
        # })
        self.name = name
        self.health = health
        self.power = power

    def get_hit(self,power):
        self.health = self.health - power
        print(f"I, {self.name}, was hit for {power} points, and now have:\n {self.health} health!")

    def attack(self,enemy):
        enemy.get_hit(self.power)

hero = Mob("Sir Barksalot",30,1)
bad_guy = Mob("EvilMcEvil",10,3)

print(hero.health)
print(bad_guy.health)

bad_guy.attack(hero)

hero.attack(bad_guy)
hero.attack(bad_guy)
hero.attack(bad_guy)
# -- -- -- 


