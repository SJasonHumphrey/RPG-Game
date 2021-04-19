# In this simple RPG game, the hero fights the goblin. He has the options to:

import random

class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        if enemy.armor == 0:
            enemy.health -= self.power
            new_power = self.power
        elif enemy.armor == 2:
            enemy.health -= self.power -1
            new_power = self.power -1
        elif enemy.armor == 4:
            enemy.health -= self.power -2
            new_power = self.power -2
        elif enemy.armor == 6:
            enemy.health -= self.power -3
            new_power = self.power -3
        elif enemy.armor == 8:
            enemy.health -= self.power -4
            new_power = self.power -4
        elif enemy.health == 10:
            enemy.health -= self.power -5
            new_power = self.power -5
        print(f'{self.name} does {new_power} damage!')

    def alive(self):
        if self.health > 0:    
            return True
        else:
            print(f'{self.name} is dead.')
            return False

    def status(self):
        print('{} has {} health and {} power'.format(self.name, self.health, self.power))

    def getItem(self, item):
        pass

class Store(Character):

    def SuperTonic(self):
        self.health = 50
        self.cost = 2

    def Armor(self):
        self.armor + 2
        self.cost = 2

    def Evade(self):
        self.evade + 2
        self.cost = 3
    



class Hero(Character):
    def __init__(self, health, power, armor=0):
        super(Hero, self).__init__(health, power, armor)
        self.name = 'Hero'
        self.armor = 0
        self.evade = 0


    def attack(self, enemy):
        double = random.random()
        if double > 0.2:
            print('You unlocked double damage!')
            enemy.health -= self.power * 2
            print('You did {} damage to the {}'.format(self.power * 2, enemy.name))
        else:
            enemy.health -= self.power
            print('You do {} damage to the {}'.format(self.power, enemy.name))
        
class Goblin(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Goblin'
        self.bounty = 4

class Shadow(Character):
    def __init__(self, health, power, bounty):
        super().__init__(health, power, bounty)
        self.name = 'Shadow'
        self.bounty = 10


class Medic(Character):
    def __init__(self, health, power, bounty):
        super(Medic, self).__init__(health, power, bounty)
        self.name = "Medic"
        self.bounty = 1


class Wizard(Character):
    def __init__(self, health, power, bounty):
        super(Wizard, self).__init__(health, power, bounty)
        self.name = 'Wizard'
        self.bounty = 4 

class Zombie(Character):
    def __init__(self, health, power, bounty):
        super(Zombie, self).__init__(health, power, bounty)
        self.name = 'Zombie'
        self.bounty = 0

    def alive(self):
        return True 


def main():
    bounty = 5

    hero = Hero(6,10,6)
    goblin = Goblin(12,4,4)
    zombie = Zombie(100,4,0)
    medic = Medic(20,5,1)
    shadow = Shadow(0,1,6)
    wizard = Wizard(15,8,4)


    enemyList = [goblin, zombie, medic, shadow, wizard]
    enemy = random.choice(enemyList)

    while hero.alive() and enemy.alive():
        print(hero.status())
        print(enemy.status())
        print()
        print("What do you want to do?")
        print("1. Fight {}".format(enemy.name))
        print("2. Do nothing")
        print("3. Flee")
        print("4. Bounty")
        print("5. Store")
        print("6. Exit")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == '1':
            if enemy.name == "medic":
                health = random.random()
                if health > 0.2:
                    hero.attack(enemy)
                else:
                    hero.attack(enemy)
                    (medic.health + 2)
                    print("Medic has recuperated 2 health!")
            elif enemy.name == "shadow":
                strike = random.randint(0,100)
                if strike > 90:
                    hero.attack(enemy)
                    print("you struck Shadow")
                else:
                    print('You missed Shadow!')
            else:
                hero.attack(enemy)
            if enemy.alive():
                enemy.status()
            else:
                print('Collected {} Bounty'.format(enemy.bounty))
                bounty += enemy.bounty
        elif raw_input == "2":
            print('Found an enemy!')
            evade = random.randint(0,100)
            enemy = random.choice(enemyList) 
            if hero.evade == 0:
                enemy.attack(hero)
            elif hero.evade == 2:
                if evade < 90:
                    enemy.attack(hero)
                else:
                    print("Enemy missed!")
            elif hero.evade >= 4 and hero.evade <= 6:
                if evade < 85:
                    enemy.attack(hero)
                else:
                    print("Enemy missed!")        
            elif hero.evade >= 8 and hero.evade <= 10:
                if evade < 75:
                    enemy.attack(hero)
                else:
                    print("Enemy missed!")
        elif raw_input == "3":
            print('Goodbye')
            break
        elif raw_input == "4":
            print(f'Your bounty total is {bounty} coins')
        elif raw_input == "5":
            print("What would you like?")
            print('Supertonic \nArmor\nEvade\nStrength')
            choice = input('Choose item to purchase: ')
            if choice == "Armor":
                if bounty < 2:
                    print('You do not have enough coins')
                else:
                    hero.armor += 2
                    print(f'Armor increased to {hero.armor}')
            elif choice == "SuperTonic":
                hero.health = 50
                if bounty < 2:
                    print('You do not have enough coins')
                else:
                    bounty -= 2
                    print('Full health restored!')
            elif choice == "Gym membership":
                hero.power += 3
                if bounty < 4:
                    print('You do not have enough coins')
                else:
                    bounty -= 4
                    print('Power increased to {}'.format(hero.power))
            elif choice == "Evade":
                if hero.evade <= 8:
                    if bounty < 2:
                        print('You do not have enough coins')
                    else:
                        hero.evade += 2
                        print(f'Evade increased to {hero.evade}')
                else:
                    print(f'Hero evade is {hero.evade}')
                    print('MAX EVADE REACHED')
        elif raw_input == "6":
            exit()
        else:
            print("Invalid input {}".format(raw_input))
        


main()