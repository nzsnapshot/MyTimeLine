import json 
from equipment import Weapon


def insert_if_not(equipment, equip_type):
    file = 'data.json'
    word = equip_type
    with open(file) as f:
        data = json.loads(f.read())
    check_if = data[equipment]
    for x in check_if:
        if equip_type in x:
            print(f"{equip_type.lower()} is already in the database!")
        else:
            with open('data.json') as json_file: 
                data = json.load(json_file) 
                for k, v in data.items():
                    x = v[0]
                x.update({word : []})
            with open(file,'w') as f: 
                json.dump(data, f, indent=4)
                print(f"We have added {equip_type} to the json file under {equipment}")
            

def check_item_exists(equipment, equip_type, item_search, item_category):
    file = 'data.json'
    with open(file) as f:
        data = json.loads(f.read())

    check_if = data[equipment.lower()][0] # Weapons            
    test = check_if[equip_type.lower()] # Weapons - Melee weapons
    try:
        for x in test: # Loops through the melee_weapons list
            if item_search in x[item_category]: # Checks for all weapons in weapon_name
                return True
    except KeyError:
        pass


def add_weapon(equipment,equip_type, wep_name,minimum,maximum,wep_type):
    insert_if_not(equipment.lower(), equip_type.lower())
    check = check_item_exists(equipment, equip_type, wep_name, "weapon_name")
    if check != True:
        filename='data.json'
        with open('data.json') as json_file: 
            data = json.load(json_file)
            temp = data[equipment.lower()][0]
            temp1 = temp[equip_type.lower()]
            # python object to be appended 
            y = {"weapon_name": wep_name.lower(), 
                "min_damage": minimum, 
                "max_damage": maximum,
                "wep_type": wep_type.lower()
                } 
            # appending data to emp_details  
            temp1.append(y) 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4)
    else:
        print("This item is already in the system")


# add_weapon("weapons", "MELEE_WEAPON", "Fists", 1, 2, "KNUCKLES")


def add_armour(armour_name, armourHealth, armourType):
    filename='data.json'
    with open('data.json') as json_file: 
        data = json.load(json_file) 
        
        temp = data['armour'][''] 
    
        # python object to be appended 
        y = {"armour_name": armour_name, 
            "armour_health": armourHealth,
            "armour_type": armourType
            } 
        # appending data to emp_details  
        temp.append(y) 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 


if __name__ == "__main__":
    add_weapon()