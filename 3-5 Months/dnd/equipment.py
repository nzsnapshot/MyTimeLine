import random
import time

# That will tidy shit up. Just take the color. You can see under def print_weapon()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

red = color.RED
end = color.END
bold = color.BOLD
purple = color.PURPLE
green = color.GREEN





class Weapon:
    def __init__(self, minDamage, maxDamage, weaponType):
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.type = weaponType

    def print_weapon(self, wep_type):
        print(f"\n{bold}Attack Style: {wep_type}{end}"
              f"\n{green}Weapon:{end} {self.type}" 
              f"\n{green}Damage:{end} {self.minDamage} - {self.maxDamage}\n") 

    def return_damage(self):
        return self.minDamage, self.maxDamage





class Armour:
    def __init__(self, armourHealth, armourType):
        self.armourHealth = armourHealth
        self.type = armourType

    def print_armour(self):
        print(f"{color.PURPLE}Armour Type:{color.END}  {self.type}\n"
              f"\033[1;33;40mArmour:\033[0;0m  {self.armourHealth}\n")

    def return_armour(self):
        return self.armourHealth, self.type

















if __name__ == "__main__":
    Armour()
    Weapon()