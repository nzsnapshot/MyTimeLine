import json

with open('test.json') as f:
    item = json.load(f)
    
for weapon in item:
    min = item[weapon][0]
    max = item[weapon][1]
    style = item[weapon][2]
    
    if style.lower() == "magic":
        print(f'Weapon: {weapon.title()}\n'
            f'Min: {min}\n'
            f'Max: {max}\n'
            f'Style: {style}\n')
