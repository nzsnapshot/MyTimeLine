import json
import collections
import os
import csv


# alldicts = []
# def pull_json(path):
#     for file in os.listdir(path):
#         full_filename = "%s/%s" % (path, file)
#         with open(full_filename,'r') as fi:
#             dict = json.load(fi)
#             alldicts.append(dict)


# 1ST USE THIS TO GET ALL THE JSON FILES YOU SCRAPPED
# path = '/Users/Snapshot/PycharmProjects/runescape/runescape/playerscraper'
# pull_json(path)

# def csv_file(filename, dumpfile):
#     readable_file = filename
#     with open(readable_file, 'w') as f:
#         json.dump(dumpfile, f, indent=4)

# 2nd USE THIS TO RECREATE THE MULTIPLE JSON FILES
# csv_file('first_pk_wanker.json', alldicts)

# 3rd We load the json file we just created
filename = 'first_pk_wanker.json'
with open(filename) as f:
    alldicts = json.load(f)

# 4th Once this file is loaded we begin to make the lists for all the data inside.
combats, usernames, head, weapon, shield, hands, torso, legs, boots, amulet, cape = [], [], [], [], [], [], [], [], [], [], []

def checkappend(appendto: list, fromdict: dict, key: str,):
    if key in fromdict:
        appendto.append( fromdict[key] )

# Loop through the players dictionaries
for i in alldicts:
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

slots(weapon_id, weapon, 'name')
slots(torso_id, torso, 'name')
slots(legs_id, legs, 'name')
slots(boots_id, boots, 'name')
slots(cape_id, cape, 'name')
slots(amulet_id, amulet, 'name')
slots(shield_id, shield, 'name')
slots(hands_id, hands, 'name')

combat_coll = collections.Counter(combats)

torso_coll = collections.Counter(torso_id)
weapon_coll = collections.Counter(weapon_id)
legs_coll = collections.Counter(legs_id)
boots_coll = collections.Counter(boots_id)
cape_coll = collections.Counter(cape_id)
amulet_coll = collections.Counter(amulet_id)
shield_coll = collections.Counter(shield_id)
hands_coll = collections.Counter(hands_id)

print(torso_coll)
print(hands)

with open('hands.csv','w') as f:
    w = csv.writer(f)
    w.writerows(hands_coll.items())

