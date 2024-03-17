import sys
import json
from functools import reduce
from app.models import Character, Ability, Background, Alignment, Cls_5e, Race, Location, Ladder, Skill, Feat, Rank, Faction, Damagetype, Feature, File
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
        
    def get_file(id):
        file = File.query.get(id)
        return file
        
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
        margin = 20
        folder_dict = {}
        name_dict = {}
        name_tracker = []
        object_tracker = []
        cur_par = root
        name_tracker.append(cur_par.name)
        object_tracker.append(cur_par)
        folder_dict[cur_par] = [len(cur_par.children_dirs), cur_par.children_dirs, margin]
        Setter.set_folders(name_dict, name_tracker, object_tracker, margin)
        folders_left = folder_dict[cur_par][0]
        while folders_left != 0:
            if folder_dict[cur_par][0] == 0:
                folder_dict[cur_par.parent_dir[0]][0] -= 1
            if folder_dict[cur_par][0] != 0:
                margin += 20
                cur_par = folder_dict[cur_par][1][len(folder_dict[cur_par][1]) - folder_dict[cur_par][0]]
                name_tracker.append(cur_par.name)
                object_tracker.append(cur_par)
                Setter.set_folders(name_dict, name_tracker, object_tracker, margin)
                folder_dict[cur_par] = [len(cur_par.children_dirs), cur_par.children_dirs, margin]
            else:
                margin -= 20
                name_tracker.pop()
                object_tracker.pop()
                cur_par = cur_par.parent_dir[0]
            folders_left = 0
            for v in folder_dict.values():
                folders_left += v[0]  
        return name_dict
    

class Setter:

    def set_folders(dict_t, name_keys, object_keys, mar):
        for n_key, o_key in zip(name_keys, object_keys):
            if n_key not in dict_t:
                dict_t[n_key] = {'name': o_key.name, 'type': 'folder', 'margin': mar}
                for file in o_key.files:
                    dict_t[n_key][file.name] = {'name': file.name, 'type': 'file', 'margin': mar}
            dict_t = dict_t[n_key]
        return dict_t

class Organizer:

    def reorder_keys(d, key_order):
        if isinstance(d, dict):
            return {k: Organizer.reorder_keys(d.get(k), key_order) for k in key_order if k in d}
        elif isinstance(d, list):
            return [Organizer.reorder_keys(x, key_order) for x in d]
        else:
            return d
        
class JsonTools:

    def find_path(json_obj, value, path=()):
        if isinstance(json_obj, dict):
            for k, v in json_obj.items():
                new_path = JsonTools.find_path(v, value, path + (k,))
                if new_path is not None:
                    return new_path
        elif isinstance(json_obj, list):
            for i, v in enumerate(json_obj):
                new_path = JsonTools.find_path(v, value, path + (i,))
                if new_path is not None:
                    return new_path
        elif json_obj == value:
            return path

    def path_to_string(path):
        return json.dumps(path)

    def string_to_path(path_string):
        return json.loads(path_string)
    
    def get_value_by_path(json_obj, path):
        for key in path:
            if isinstance(key, int):
                json_obj = json_obj[key]
            else:
                json_obj = json_obj.get(key)
        return json_obj
    
    def replace_value_by_path(json_obj, path, new_value):
        *path, last_key = path
        for key in path:
            if isinstance(key, int):
                json_obj = json_obj[key]
            else:
                json_obj = json_obj.get(key)
        if isinstance(last_key, int):
            json_obj[last_key] = new_value
        else:
            json_obj[last_key] = new_value  