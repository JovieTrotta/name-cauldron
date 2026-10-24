# IMPORTS
import random

# FUNCTIONS
def get_dic_choice(race, gender, affix):
    choice = random.choice(list(race[gender][affix]))
    return choice

def make_name(pre, suf):
    name = pre + suf
    return name

def make_definition(race, gender, affix, key):
    definition = (race[gender][affix][key])
    return definition