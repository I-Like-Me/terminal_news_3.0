import sys
import json
from functools import reduce
from app.models import Character, Ability, Background, Alignment, Cls_5e, Race, Location, Ladder, Skill, Feat, Rank, Faction, Damagetype, Feature, Folder, File
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
        margin = 20
        final_order = []
        item_dict = {}
        name_dict = {}
        dict_tracker = []
        cur_item = root
        final_order.append(cur_item)
        dict_tracker.append(cur_item.name)
        item_dict[cur_item] = [len(cur_item.children_dirs), cur_item.children_dirs, len(cur_item.files), cur_item.files, margin]
        name_dict[cur_item.name] = {'margin': margin}
        items_left = item_dict[cur_item][0] + item_dict[cur_item][2]
        loop = 0
        # while items_left != 0:
        #     print('--Start--')
        #     print(f'Loop {loop}')
        #     print(cur_item)
        #     if type(cur_item) == Folder and item_dict[cur_item][0] == 0:
        #         print('mark')
        #         item_dict[cur_item.parent_dir[0]][0] -= 1
        #     if type(cur_item) == File and item_dict[cur_item.parent_dir[0]][2] != 0:
        #         print('kevin')
        #         item_dict[cur_item.parent_dir[0]][2] -= 1
        #     if type(cur_item) == Folder:
        #         if item_dict[cur_item][0] != 0:
        #             print('sue')
        #             margin += 20
        #             step += 1
        #             cur_item = item_dict[cur_item][1][len(item_dict[cur_item][1]) - item_dict[cur_item][0]]
        #             final_order.append(cur_item)
        #             dict_tracker.append(cur_item.name)
        #             Setter.set_folders(name_dict, dict_tracker, margin, 'folder')
        #             item_dict[cur_item] = [len(cur_item.children_dirs), cur_item.children_dirs, len(cur_item.files), cur_item.files, margin]
        #         elif item_dict[cur_item][0] == 0 and item_dict[cur_item][2] != 0:
        #             print('stan')
        #             cur_item = item_dict[cur_item][3][len(item_dict[cur_item][3]) - item_dict[cur_item][2]]
        #             final_order.append(cur_item)
        #             dict_tracker.append(cur_item.name)
        #             Setter.set_folders(name_dict, dict_tracker, margin, 'file')
        #             # item_dict[cur_item] = cur_item.name
        #     else:
        #         if type(cur_item) == File:
        #             print('reese')
        #             margin -= 20
        #             step -= 1
        #             dict_tracker.pop()
        #             cur_item = cur_item.parent_dir[0]
        #         if type(cur_item) == Folder:
        #             while item_dict[cur_item][0] == 0:
        #                 print('luke')
        #                 margin -= 20
        #                 step -= 1
        #                 dict_tracker.pop()
        #                 cur_item = cur_item.parent_dir[0]
        #     items_left = 0
        #     for v in item_dict.values():
        #         print(v)
        #         folders_left = v[0]
        #         files_left = v[2] 
        #         print(f'{folders_left} folders left and {files_left} files left')
        #         both = folders_left + files_left
        #         items_left += both
        #     loop += 1
        while items_left != 0:
            print('--Start--')
            # print(final_order)
            print(name_dict)
            print(cur_item)
            # print(item_dict)
            # print(items_left)
            # print(name_dict)
            if type(cur_item) == Folder:
                # if item_dict[cur_item][0] == 0 and item_dict[cur_item][2] == 0:
                #     item_dict[cur_item.parent_dir[0]][0] -= 1
                if item_dict[cur_item][0] > 0:
                    print('red')
                    margin += 20
                    step += 1
                    cur_item = item_dict[cur_item][1][len(item_dict[cur_item][1]) - item_dict[cur_item][0]]
                    final_order.append(cur_item)
                    dict_tracker.append(cur_item.name)
                    Setter.set_folders(name_dict, dict_tracker, margin)
                    if cur_item not in item_dict:
                        item_dict[cur_item] = [len(cur_item.children_dirs), cur_item.children_dirs, len(cur_item.files), cur_item.files, margin]
                    if item_dict[cur_item][0] == 0 and item_dict[cur_item][2] == 0:
                        item_dict[cur_item.parent_dir[0]][0] -= 1
                elif item_dict[cur_item][0] == 0 and item_dict[cur_item][2] > 0:
                    print('green')
                    print(item_dict[cur_item][2])
                    final_order.append(item_dict[cur_item][3][len(item_dict[cur_item][3]) - item_dict[cur_item][2]])
                    dict_tracker.append(item_dict[cur_item][3][len(item_dict[cur_item][3]) - item_dict[cur_item][2]].name)
                    Setter.set_folders(name_dict, dict_tracker, margin)
                    print(item_dict[cur_item.parent_dir[0]][2])
                    item_dict[cur_item][2] -= 1
                else:
                    print('blue')
                    while item_dict[cur_item][0] == 0 and item_dict[cur_item][2] == 0:
                        margin -= 20
                        step -= 1
                        dict_tracker.pop()
                        cur_item = cur_item.parent_dir[0]
                items_left = 0
                for v in item_dict.values():
                    items_left += v[0] + v[2]
        return name_dict
    
class Setter:
    
    def set_folders(dict_n, keys, mar):
        for key in keys:
            if key not in dict_n:
                dict_n[key] = {'margin': mar}
            dict_n = dict_n[key]
        return dict_n
    
    def set_files(dict_n, keys):
        print(dict_n)
        for key in keys:
            if key not in dict_n:
                dict_n[key] = key
            dict_n = dict_n[key]
        return dict_n


    
