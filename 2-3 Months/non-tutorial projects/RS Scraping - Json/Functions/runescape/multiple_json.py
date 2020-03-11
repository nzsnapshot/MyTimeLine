import json
import collections
import csv

filename = 'data.json'
with open(filename) as f:
    all_player_data = json.load(f)

with open('readable_eq_data.json') as f:
    summary = json.load(f)

# filename = '/Users/Snapshot/PycharmProjects/runescape/runescape/summary.json'
# with open(filename) as f:
#     summary = json.load(f)
#
#
readable_file = 'readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(summary, f, indent=4)


#Player Dictionary
player_dict = all_player_data

# Variables which I use to store the lists in.
combats, usernames, head, weapon, shield, hands, torso, legs, boots, amulet, cape = [], [], [], [], [], [], [], [], [], [], []

def checkappend(appendto: list, fromdict: dict, key: str,):
    if key in fromdict:
        appendto.append( fromdict[key] )

my_dict = summary

my_list = []
for s in my_dict:
    if '' in s:
        checkappend(my_list, s[''], 'buy_average')
print(my_dict)

# Loop through the players dictionaries
for i in player_dict:
    checkappend(usernames, i, 'name'        )
    checkappend(combats,   i, 'combat_level')
    if 'items' in i:
        checkappend(weapon, i['items'], 'weapon')
        checkappend(hands,  i['items'], 'hands' )
        checkappend(shield, i['items'], 'shield')
        checkappend(torso, i['items'], 'torso')
        checkappend(legs, i['items'], 'legs')
        checkappend(boots, i['items'], 'boots')
        checkappend(cape, i['items'], 'cape')
        checkappend(amulet, i['items'], 'amulet')

def appending(appendto: list, fromdict: dict, key: str,):
    if key in fromdict:
        appendto.append( fromdict[key] )

weapon_id = []
torso_id = []
legs_id = []
boots_id = []
cape_id = []
amulet_id = []
shield_id = []
hands_id = []

def slots(identification, slot, id):
    for x in slot:
        appending(identification, x, id)

slots(weapon_id, weapon, 'id')
slots(torso_id, torso, 'id')
slots(legs_id, torso, 'id')
slots(boots_id, torso, 'id')
slots(cape_id, torso, 'id')
slots(amulet_id, torso, 'id')
slots(shield_id, torso, 'id')
slots(hands_id, torso, 'id')

torso_coll = collections.Counter(torso_id)
weapon_coll = collections.Counter(weapon_id)
legs_coll = collections.Counter(legs_id)
boots_coll = collections.Counter(boots_id)
cape_coll = collections.Counter(cape_id)
amulet_coll = collections.Counter(amulet_id)
shield_coll = collections.Counter(shield_id)
hands_coll = collections.Counter(hands_id)





# with open('hands_coll.csv','w') as f:
#     w = csv.writer(f)
#     w.writerows(hands_coll.items())