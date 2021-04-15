# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    
    def attack(self, enemy):
        enemy.health -= self.power
        print('{} did {} damage!'.format(self.name, self.power))

    def print_status(self):
        print('{} has {} health and {} power.'.format(self.name, self.health, self.power))

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Hero(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    # def attack(self, enemy, name):
    #     enemy.health -= self.power
    #     ('The Goblin did {} damage to the you'.format(self.power))

    # def print_status(self):
    #     print("You have {} health and {} power.".format(self.health, self.power))

    # def alive(self):
    #     if self.health > 0:
    #         print("You have {} health and {} power.".format(self.health, self.power))


class Enemy(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print('You did {} damge to the Goblin'.format(self.power))

    # def print_status(self):
    #     print("The Goblin has {} health and {} power.".format(self.health, self.power))

    # def alive(self):
    #     if self.health > 0:
    #         print("The goblin has {} health and {} power.".format(self.health, self.power))

class Zombie(Character):
    def __init__(self, name):
        pass

def main():
    hero = Hero(10, 5, 'Hero')
    goblin = Enemy(6, 2, 'Goblin')


    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight Goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input=input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            # goblin.health -= hero.power
            # print("You do {} damage to the goblin.".format(hero.power))
            if not goblin.alive():
                print("The Goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
            hero.health -= goblin.power
            # print("The {} does {} damage to you.".format(goblin.name,goblin.power))
            if not hero.alive():
                print("You are dead.")

main()
