import json


filename = '/Users/Snapshot/PycharmProjects/runescape/runescape/readable_eq_data.json'
with open(filename) as f:
    summary = json.load(f)

###############################################################################
# Helper methods
def _strcast(val):
    """ Convert value to string. """
    if val is None:
        return None
    return str(val)


def _intcast(val):
    """ Convert input to integer. """
    if val is None:
        return None
    if isinstance(val, int):
        return val
    if isinstance(val, str):
        return int(val)


###############################################################################
class PlayerScraper(object):
    def __init__(self):
        # Dict of all ItemDefinition properties
        self.properties = {
            "player": None,
            "world": None,
            "combat": None,
            "head": None,
            "cape": None,
            "amulet": None,
            "weapon": None,
            "torso": None,
            "shield": None,
            "legs": None,
            "hands": None,
            "boots": None}

        # Below are lists to help automate parsing of JSON file
        # Some items are nested in the JSON structure
        self.not_nested = [
            "player",
            "world",
            "combat"]

        self.nested = [
            "head",
            "cape",
            "amulet",
            "weapon",
            "torso",
            "shield",
            "legs",
            "hands",
            "boots"]

        self.nested_cost = [
            "cost_head",
            "cost_cape",
            "cost_amulet",
            "cost_weapon",
            "cost_torso",
            "cost_shield",
            "cost_legs",
            "cost_hands",
            "cost_boots"]

        ###############################################################################

    # Setters and Getters
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = _strcast(value)

    @property
    def world(self):
        return self._world

    @world.setter
    def world(self, value):
        self._world = _intcast(value)

    @property
    def combat(self):
        return self._combat

    @combat.setter
    def combat(self, value):
        self._combat = _intcast(value)

        # Equipment slots

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = _intcast(value)

    @property
    def cape(self):
        return self._cape

    @cape.setter
    def cape(self, value):
        self._cape = _intcast(value)

    @property
    def amulet(self):
        return self._amulet

    @amulet.setter
    def amulet(self, value):
        self._amulet = _intcast(value)

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, value):
        self._weapon = _intcast(value)

    @property
    def torso(self):
        return self._torso

    @torso.setter
    def torso(self, value):
        self._torso = _intcast(value)

    @property
    def shield(self):
        return self._shield

    @shield.setter
    def shield(self, value):
        self._shield = _intcast(value)

    @property
    def legs(self):
        return self._legs

    @legs.setter
    def legs(self, value):
        self._legs = _intcast(value)

    @property
    def hands(self):
        return self._hands

    @hands.setter
    def hands(self, value):
        self._hands = _intcast(value)

    @property
    def boots(self):
        return self._boots

    @boots.setter
    def boots(self, value):
        self._boots = _intcast(value)

        # Equipment slot costs

    @property
    def cost_head(self):
        return self._cost_head

    @cost_head.setter
    def cost_head(self, value):
        self._cost_head = _intcast(value)

    @property
    def cost_cape(self):
        return self._cost_cape

    @cost_cape.setter
    def cost_cape(self, value):
        self._cost_cape = _intcast(value)

    @property
    def cost_amulet(self):
        return self._cost_amulet

    @cost_amulet.setter
    def cost_amulet(self, value):
        self._cost_amulet = _intcast(value)

    @property
    def cost_weapon(self):
        return self._cost_weapon

    @cost_weapon.setter
    def cost_weapon(self, value):
        self._cost_weapon = _intcast(value)

    @property
    def cost_torso(self):
        return self._cost_torso

    @cost_torso.setter
    def cost_torso(self, value):
        self._cost_torso = _intcast(value)

    @property
    def cost_shield(self):
        return self._cost_shield

    @cost_shield.setter
    def cost_shield(self, value):
        self._cost_shield = _intcast(value)

    @property
    def cost_legs(self):
        return self._cost_legs

    @cost_legs.setter
    def cost_legs(self, value):
        self._cost_legs = _intcast(value)

    @property
    def cost_hands(self):
        return self._cost_hands

    @cost_hands.setter
    def cost_hands(self, value):
        self._cost_hands = _intcast(value)

    @property
    def cost_boots(self):
        return self._cost_boots

    @cost_boots.setter
    def cost_boots(self, value):
        self._cost_boots = _intcast(value)

        ###########################################################################

    # Processing functions
    def load(self, fi):
        # print(">>> Loading player file...")
        with open(fi) as f:
            input = json.load(f)

        # print(">>> Populating player, combat and world...")
        for prop in self.not_nested:
            setattr(self, prop, input[prop])

            # print(">>> Populating player equipment...")
        for prop in self.nested:
            try:
                setattr(self, prop, input[prop]["id"])
            except KeyError:
                setattr(self, prop, None)

        self.is_naked = False
        equiped_count = 0
        for prop in self.nested:
            attr = getattr(self, prop)
            if attr is not None:
                equiped_count += 1
        if equiped_count == 0:
            self.is_naked = True

        return self

    def calc_wealth(self, summary, allitems):
        # Determine the total wealth of player equipment items
        # Also determine the cost for each slot

        # Determine total wealth (sum all item slots)
        current_wealth = 0
        for prop in self.nested:
            id = str(getattr(self, prop))
            if id is None:
                continue

            try:
                item_wealth = summary[id]["overall_average"]
            except KeyError:
                item_wealth = 0

            if item_wealth == 0:
                try:
                    item_wealth = allitems[id]["cost"]
                except KeyError:
                    item_wealth = 0

            # Put item wealth into cost_"prop"
            new_prop = "cost_" + prop
            setattr(self, new_prop, item_wealth)
            current_wealth += item_wealth

        self.wealth = current_wealth

play = PlayerScraper.calc_wealth(None, summary, )