import json
import collections
import csv


# # Open my items_itemscraper.json file (my file with cost and alch prices)
# with open("items_itemscraper.json") as f:
#     allitems = json.load(f)
#
# # Open OSBuddy's summary.json file about item prices
# with open("summary.json") as f:
#     summary = json.load(f)







# Json file for all players
filename = 'all-players.json'
with open(filename) as f:
    all_player_data = json.load(f)


combats, usernames, head, weapon, shield, hands, torso, legs, boots, amulet, cape  = [], [], [], [], [], [], [], [], [], [], []

player_dict = all_player_data['features']
for i in player_dict:
    try:
        combat = i['combat']
        gear_head = i['head']['name']
        gear_weapon = i['weapon']['name']
        gear_shield = i['shield']['name']
        gear_hands = i['hands']['name']
        gear_torso = i['torso']['name']
        gear_legs = i['legs']['name']
        gear_boots = i['boots']['name']
        gear_amulet = i['amulet']['name']
        gear_cape = i['cape']['name']
        user = i['player']
    except KeyError:
        pass
    else:
        combats.append(combat)
        head.append(gear_head)
        usernames.append(user)
        weapon.append(gear_weapon)
        shield.append(gear_shield)
        hands.append(gear_hands)
        torso.append(gear_torso)
        legs.append(gear_legs)
        boots.append(gear_boots)
        amulet.append(gear_amulet)
        cape.append(gear_cape)

count_head = collections.Counter(head)
count_weapon = collections.Counter(weapon)
count_shield  = collections.Counter(shield)
count_hands  = collections.Counter(hands)
count_torso  = collections.Counter(torso)
count_legs  = collections.Counter(legs)
count_boots  = collections.Counter(boots)
count_amulet  = collections.Counter(amulet)
print(count_weapon)
print(len(combats))
print(count_shield)
print(count_torso)






# The Filename we want to write to
def write_csv(filename, dick):
    """Writing to a csv file. Make sure to include **Filename.csv**"""
    somedict = dick
    with open(filename, 'w') as f:
        w = csv.writer(f)
        w.writerows(somedict.items())










