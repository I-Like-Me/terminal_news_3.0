import sys
import json
from functools import reduce
from app.models import Character, Ability, Background, Alignment, Cls_5e, Race, Location, Ladder, Skill, Feat, Rank, Faction, Damagetype, Feature, Folder
from app.main.forms import CharacterForm, AbilityForm, FeatForm, AlignmentForm, BackgroundForm, DamagetypeForm, DiceForm, FactionForm, FeatureForm, LocationForm, PropertyForm, RankForm, SkillForm

class Converters:

    def str_to_class(str):
        return getattr(sys.modules[__name__], str)
    
class Collectors:
    def get_bin(asset_type):
        bins = {
            'Character': {'background': "Background", 'alignment': "Alignment", 
                        'classes': 'Cls_5e', 'cur_race': 'Race', 'birth_race': 'Race',
                        'cur_loc': 'Location', 'birth_loc': 'Location', 'ladder': 'Ladder',
                        'skill_pro_choice': 'Skill'}, 
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
            'Cybernetic': {'properties': "Property"},
            'Skill': {'ability': "Ability"}
        }
        if asset_type in bins:
            return bins[asset_type]
        else:
            return None
        
    def fill_bin(asset_bin):
        bin = {}
        if asset_bin is not None:
            for x, y in asset_bin.items():
                bin[f"{x}"] = Converters.str_to_class(y).query.all()
            return bin
        else:
            return None
        
class Builders:
    def build_commit(asset, data, items):
        arg_dict = {}
        for k, v in data.items():
            if k not in ['submit', 'csrf_token']:
                if k == 'name':
                    arg_dict[k] = v.lower()
                else:
                    if k in items:
                        if isinstance(data[k], Converters.str_to_class(items[k])):
                            v = [v]
                            arg_dict[k] = v
                        else:
                            arg_dict[k] = v
                    else:
                        arg_dict[k] = v
        table_name = Converters.str_to_class(f'{asset}')
        new_asset = table_name(**arg_dict)
        return new_asset

    def build_structure(root):
        step = 0
        margin = 0
        final_order = []
        folder_dict = {}
        name_dict = {}
        dict_tracker = []
        cur_par = root
        final_order.append(cur_par)
        dict_tracker.append(cur_par.name)
        folder_dict[cur_par] = [len(cur_par.children_dirs), cur_par.children_dirs, margin]
        name_dict[cur_par.name] = {}
        folders_left = folder_dict[cur_par][0]
        while folders_left != 0:
            print(folder_dict[cur_par][2])
            print(cur_par)
            print(dict_tracker)
            print(step)
            print(name_dict)
            if folder_dict[cur_par][0] == 0:
                folder_dict[cur_par.parent_dir[0]][0] -= 1
            if folder_dict[cur_par][0] != 0:
                margin += 20
                step += 1
                cur_par = folder_dict[cur_par][1][len(folder_dict[cur_par][1]) - folder_dict[cur_par][0]]
                final_order.append(cur_par)
                dict_tracker.append(cur_par.name)
                Setter.set_folders(name_dict, dict_tracker, cur_par)
                folder_dict[cur_par] = [len(cur_par.children_dirs), cur_par.children_dirs, margin]
            else:
                margin -= 20
                step -= 1
                dict_tracker.pop()
                cur_par = cur_par.parent_dir[0]
            folders_left = 0
            for v in folder_dict.values():
                folders_left += v[0]  
        return name_dict
    
    def build_child_list(cur_p):
        for c in cur_p.children_dirs:
            return c
    
class Setter:
    
    def set_folders(dict_t, keys, cur_p):
        for key in keys:
            if key not in dict_t:
                dict_t[key] = {}
            dict_t = dict_t[key]
        return dict_t
            


    
