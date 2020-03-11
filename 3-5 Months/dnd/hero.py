# I've never made a game like this before or thought of. 
# Hope you dont mind me trying to build one here
# Always better to code with others
import random
import time
from equipment import Weapon, Armour
import json_add
from colour import color

red = color.RED
end = color.END
bold = color.BOLD


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
     
    def print_hero(self):
        print(f"\033[1;34;40mHeroes Name:\033[0;0m {self.name}\n" 
              f"Heroes Health: {self.health}\n")         

    def attack(self, weapon):
        minimum = weapon.return_damage()[0]
        maximum = weapon.return_damage()[1]
        damage = random.randrange(minimum, maximum)
        print(f"You hit: {bold}{red}{damage}{end}\n")


        




# weapon_type = ['Melee', 'Range', 'Magic']

# """Range Weapons"""
# short_bow = Weapon(3, 10, "Bow")
# long_bow = Weapon(5, 12, "Bow")
# ogre_bow = Weapon(10, 15, "Bow")

# """Melee Weapons"""
# dagger = Weapon(3, 5, "Dagger")
# long_sword = Weapon(5, 12, "Sword")
# lance = Weapon(10, 15, "Lance")
# great_sword = Weapon(10, 15, "Greater_Sword")

# """Magic Weapons"""
# beginner_staff = Weapon(1, 69, "Stick")
# master_staff = Weapon(15, 17, "Master Staff")
# beginner_wand = Weapon(3, 5, "Wand")
# master_wand = Weapon(15, 17, "Master Wand")


# # range_weapons = {
# #     short_bow:'ranging', 
# #     long_bow:'ranging', 
# #     ogre_bow:'ranging'
# #     }

# # print(range_weapons[0])

# range_weapons = [short_bow, long_bow, ogre_bow]
# melee_weapons = [dagger, long_sword, lance, great_sword]
# magic_weapons = [beginner_staff, master_staff, beginner_wand, master_wand]

# ''' Uses random.choice to pick a random instanced weapon '''
# melee_rand = random.choice(melee_weapons)
# range_rand = random.choice(range_weapons)
# magic_rand = random.choice(magic_weapons)


# # # hero_melee = Hero('Adrino')
# # # hero_range = Hero('Archer')

# weapon = random.choice([melee_rand, range_rand, magic_rand])

# x = Hero('Baba Knush', 100)

# if weapon in melee_weapons:
#     weapon.print_weapon(weapon_type[0])
#     x.attack(weapon)
# elif weapon in range_weapons:
#     weapon.print_weapon(weapon_type[1])
#     x.attack(weapon)
# elif weapon in magic_weapons:
#     weapon.print_weapon(weapon_type[2])
#     x.attack(weapon)
# else:
#     print("No you're not a dragon today, Harry!")





