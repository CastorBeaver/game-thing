import random
#cool
class player():
    def __init__(self,name,pronouns,h = 100,a = 0):
        self.name = name
        self.pronouns = pronouns
        self.health = h
        self.armour = a

    def player_stats(self):
        print('Name:', self.name)
        print('Pronouns:', self.pronouns)
        print('Max HP:', self.health)
        print('Armour:', self.armour)
# Player class with print stats function

class sword():
    def __init__(self,damage,durability,critchance):
        self.damage = damage
        self.durability = durability
        self.critchance = critchance

    def weapon_stats(self):
        print('Damage:',self.damage)
        print('Durability:',self.durability)
# Weapon class with weapon stats function
class enemy():
    def __init__(self,name,health,damage,armour):
        self.name = name
        self.health = health
        self.damage = damage
        self.armour = armour

    def badguy(self):
        print('Health:',self.health)
        print('Damage:',self.damage)
        print('Armour:',self.armour)
# Enemy class with enemy stats function

def userdamage(weapon,badguy):
    weapon = dagger
    badguy = troll

    crit = random.randrange(-1,101,1)
    if crit <= weapon.critchance:
        damage = weapon.damage * 1.5
# Selecting random number from 1-100 and multiplying damage for a crit (if number
# chosen is lower than the weapons critchance)

    else:
        damage = weapon.damage
    if badguy.armour == 0:
        return damage
    elif badguy.armour != 0:
      damage = ((badguy.armour / 100) * damage)
      return damage
# Function for calculating how much damage a player will do each turn

def enemydamage(user,badguy):
    user = brayden
    badguy = troll

    if user.armour == 0:
        return badguy.damage
    else:
        bad_damage = ((user.armour / 100) * badguy.damage)
        return bad_damage
# Function for calculating how much damage the enemy will do each turn

def fight(user,weapon,badguy):

    user = brayden
    weapon = dagger
    badguy = troll
# Using variables instead of just the objects so later I can pass in different
# objects without having to go over code everytime
    while user.health >=0 and badguy.health >= 0:
        damage = userdamage(dagger,troll)
        print (user.name,'strikes first dealing',damage,'to',badguy.name)
        badguy.health = badguy.health - damage
        print ('The',badguy.name,'is left with',badguy.health,'health')
        if badguy.health < damage:
            damage = userdamage(dagger,troll)
            print (user.name,'strikes first dealing',damage,'to',badguy.name)
            badguy.health = badguy.health - damage
            print ('The',badguy.name,'is left with',badguy.health,'health')
            break
#hits that the player makes
        damage = enemydamage(user,badguy)
        print ('The',badguy.name,'hits back dealing',damage,'damage')
        user.health = user.health - damage
        print (user.name,'is left with',user.health,'HP!')
        if user.health < damage:
            damage = enemydamage(user,badguy)
            print ('The',badguy.name,'hits back dealing',damage,'damage')
            user.health = user.health - damage
            print (user.name,'is left with',user.health,'HP!')            
            break


# First hit in fight sequence (will have to make and input method so the user
# can chose their attack / menouver)

dagger = sword(30,100,50)
brayden = player('TridentFlyer','They/Them') 
troll = enemy('Troll',100,15,50)
# Don't know why this is here but code doesn't work without it :D

fight(brayden,dagger,troll)
# Call to fight function to test that it works
