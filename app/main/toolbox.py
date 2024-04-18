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

    def build_repr_from_path(json_obj, path):
        repr_path = []
        for key in path:
            if isinstance(key, int):
                json_obj = json_obj[key]
                repr_path.append(' > ')
            else:
                repr_path.append(json_obj.get('name'))
                json_obj = json_obj.get(key)
        return repr_path

    def path_to_string(path):
        return json.dumps(path)
    
    def repr_path_to_string(path):
        repr_str = ''.join(path) 
        return repr_str

    def string_to_path(path_string):
        return json.loads(path_string)
    
    def get_value_by_path(json_obj, path):
        for key in path:
            if isinstance(key, int):
                json_obj = json_obj[key]
            else:
                json_obj = json_obj.get(key)
        return json_obj
    
    def update_nested_dict(d, path, value):
        for p in path[:-1]:
            if isinstance(p, int):
                d = d[p]
            else:
                d = d.get(p)
        if isinstance(path[-1], int):
            d[path[-1]] = value
        else:
            d[path[-1]] = value

    def sort_nested_list(data):
        data.sort(key=lambda x: (x['type'] != 'folder', x['name']))
        for item in data:
            if item['type'] == 'folder':
                JsonTools.sort_nested_list(item['children'])

    def get_nested_dict_path(d, str_path):
        keys = str_path.split(' > ')
        result = []
        for key in keys:
            for i, child in enumerate(d['children']):
                if child['name'] == key:
                    result.extend(['children', i])
                    d = child
                    break
        return result

    def add_to_nested_dict(nested_dict, source_path, dest_path):
        # Get the item at the source path
        item = JsonTools.get_value_by_path(nested_dict, source_path)
        
        # Remove the item from its current location
        parent_path = source_path[:-2]  # Get the parent path
        parent = JsonTools.get_value_by_path(nested_dict, parent_path)  # Get the parent
        parent['children'].remove(item)  # Remove the item from the parent's children
        
        # Add the item to the destination path
        dest = JsonTools.get_value_by_path(nested_dict, dest_path)  # Get the destination
        dest['children'].append(item)  # Add the item to the destination's children
