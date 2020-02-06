############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        self.name = name
        self.code = code
        self.first_harvet = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        self.code = new_code
        """Replace the reporting code with the new_code."""

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    y_melon = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', True, True)
    y_melon.add_pairing('ice cream')
    all_melon_types.append(y_melon)

    return all_melon_types

def print_pairing_info(melon_types):
    for melon in melon_types:
        print(f'{melon.name} pairs with {melon.pairings}')
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_d = {}
    for melon in melon_types:
        melon_d[melon.code] = melon.name
    print(melon_d)
    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, type_m, shape, color, field, person):
        """Initialize a melon."""
        self.type_m = type_m
        self.shape = shape
        self.color = color
        self.field = field
        self.person = person
       
    # Fill in the rest
    def is_sellable(melon):
        if melon.shape and melon.color > 5 and melon.field != 3:

            return True

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_lst = []
    melon_1 = Melon('yw', 8, 7, 'Field 2', 'Shiela')
    melon_lst.append(melon_1)
    melon_2 = Melon('yw', 3, 4, 'Field 2', 'Shiela')
    melon_lst.append(melon_2)
    melon_3 = Melon('yw', 9, 8, 'Field 3', 'Shiela')
    melon_lst.append(melon_3)
    melon_4 = Melon('cas', 10, 6, 'Field 35', 'Shiela')
    melon_lst.append(melon_4)
    melon_5 = Melon('cren', 8, 9, 'Field 35', 'Michael')
    melon_lst.append(melon_5)
    melon_6 = Melon('cren', 8, 2, 'Field 35', 'Michael')
    melon_lst.append(melon_6)
    melon_7 = Melon('cren', 2, 3, "Field 4", "Michael")
    melon_lst.append(melon_7)
    melon_8 = Melon('musk', 6, 7, 'Field 4', "Michael")
    melon_lst.append(melon_8)
    melon_9 = Melon('yw', 7, 10, "Field 3", "Sheila")
    melon_lst.append(melon_9)
    return (melon_lst)
    # Fill in the rest

def get_sellability_report(melons):
    for melon in melons:
        if Melon.is_sellable(melon) is True:
            value = "(CAN BE SOLD)"
        else:
            value = "(NOT SELLABLE)"
        print(f"Harvested by {melon.person} from {melon.field} {value}")
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



