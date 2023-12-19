import sys
from app.models import Character
from app.main.forms import CharacterForm

class Converters:

    def str_to_class(str):
        return getattr(sys.modules[__name__], str)
    
class Collectors:

    bins = {
        'Character': {'background': "Background", 'alignment': "Alignment", 
                      'classes': 'Cls_5e', 'race': 'Race'}, 
        'Cls_5e': {'arch_choices': "Architype", 'cls_features': "Feature", 
                   "hit_dice_type": "Dice", 'tool_pros': "Gear", 
                   'weap_pros': "Weapon", 'armor_pros': "Armor", 
                   'skill_pro_choice': "Skill", 'dmg_resist': "Damagetype", 
                   'dmg_immune': "Damagetype", 'dmg_vulner': "Damagetype", 
                   'spellbook': "Spell"}, 
        'Race': {'race_features': "Feature", 'dmg_resist': "Damagetype",
                 'dmg_immune': "Damagetype", 'dmg_vulner': "Damagetype"}, 
        'Faction': {'fac_ranks': "Rank"},
        'Architype': {'arch_features': "Feature"}, 
        'Feature': {'dmg_resist': "Damagetype", 'dmg_immune': "Damagetype",
                    'dmg_vulner': "Damagetype"},
        'Weapon': {'damage_dice': "Dice", 'dmg_type': "Damagetype", 
                   'properties': "Property", 'ammo': "Ammo_power"},
        'Ammo_power': {'dmg_type': "Damagetype"},
        'Armor': {'ac_mod_type': "Ability", 'dmg_resist': "Damagetype", 
                  'dmg_immune': "Damagetype", 'dmg_vulner': "Damagetype", 
                  'power': "Ammo_power", 'properties': "Property"},
        'Gear': {'power': "Ammo_power"},
        'Vehicle': {'power': "Ammo_power", 'properties': "Property"},
        'Mech': {'power': "Ammo_power", 'properties': "Property"},
        'Cybernetic': {'properties': "Property"}
    }