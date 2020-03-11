import json
import random
from colour import color


file = 'data.json'
with open(file) as f:
    data = json.load(f)


green = color.GREEN
red = color.RED
end = color.END
bold = color.BOLD

equipment = data["weapons"][0]
ranging = equipment["range_weapon"]
ranging_count = len(ranging)
ranging_wep = ranging[random.randrange(1,ranging_count)]

melee = equipment["melee_weapon"]
melee_count = len(melee)
melee_wep = melee[random.randrange(1,melee_count)]


magic = equipment["magic_weapon"]
magic_count = len(magic)
magic_wep = magic[random.randrange(1,magic_count)]

weapon_choice = [ranging_wep, melee_wep, magic_wep]
rand = random.choice(weapon_choice)


weapon_name = f"\n{green}Weapon:{end} {rand['weapon_name']}"
weapon_damage = f"\n{green}Damage:{end} {rand['min_damage']} - {rand['max_damage']}"
weapon_min = rand['min_damage']
weapon_max = rand['max_damage']
random_damage = random.randrange(weapon_min, weapon_max)


if rand == ranging_wep:
    print(f"\n{bold}Attack Style: Range{end}")
elif rand == melee_wep:
    print(f"\n{bold}Attack Style: Melee{end}")
elif rand == magic_wep:
    print(f"\n{bold}Attack Style: Magic{end}")


print(weapon_name, weapon_damage)
print(f"\nYou hit: {red}{bold}{random_damage}{end}")

