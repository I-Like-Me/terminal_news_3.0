from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    character = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    player =
    level = db.Column(db.Integer)
    cls =
    arch = 
    ladder =
    background =
    proficiency = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    passive_perc = db.Column(db.Integer)
    armor_class = db.Column(db.Integer)
    inspiration = db.Column(db.Boolean)
    initiative = db.Column(db.Integer)
    alignment =
    cur_hit_points = db.Column(db.Integer)
    temp_hit_points = db.Column(db.Integer)
    total_hit_dice = db.Column(db.String(64))
    cur_hit_dice = db.Column(db.String(64))
    abilities =
    pro_abilities = 
    skills =
    pro_skills =
    personal_info = 
    weapons =
    gear =
    factions = 
    npc = db.Column(db.Boolean)
    parties = 
    admin = db.Column(db.Boolean)
    backpack = db.Column(db.String(5000))
    prepd_spells =
    spellbook =
    feats =
    play_notes = db.Column(db.String(5000))

class char_personal_info:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    knows_name =
    real_age = db.Column(db.Integer)
    knows_r_age =
    self_k_r_age = db.Column(db.Boolean)
    fake_age = db.Column(db.Integer)
    knows_f_age = db.Column(db.Integer)
    cur_race =
    knows_c_race = 
    birth_race =
    self_k_b_race = db.Column(db.Boolean)
    cur_race =
    birth_loc = 
    self_k_b_loc = db.Column(db.Boolean)
    cur_loc = 
    job = 
    history = db.Column(db.String(5000))
    info_subject =

class char_skill_scores:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    acrobatics = db.Column(db.Integer)
    animal_handling = db.Column(db.Integer)
    arcana = db.Column(db.Integer)
    athletics = db.Column(db.Integer)
    computer_use = db.Column(db.Integer)
    deception = db.Column(db.Integer)
    demolitions = db.Column(db.Integer)
    engineering = db.Column(db.Integer)
    history = db.Column(db.Integer)
    insight = db.Column(db.Integer)
    intimidation = db.Column(db.Integer)
    investigation = db.Column(db.Integer)
    medicine = db.Column(db.Integer)
    nature = db.Column(db.Integer)
    perception = db.Column(db.Integer)
    performance = db.Column(db.Integer)
    persuasion = db.Column(db.Integer)
    religion = db.Column(db.Integer)
    sciences = db.Column(db.Integer)
    sleight_of_hand = db.Column(db.Integer)
    stealth = db.Column(db.Integer)
    survival = db.Column(db.Integer)
    skilled_char =

class char_ability_scores:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    able_char =

class party:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    members = 
    max_members = db.Column(db.Integer)
    joined_game = 

class cls_5e:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    features =
    hit_dice_type = 
    hit_pnt_l01 = db.Column(db.Integer)
    sav_throw = 
    tool_pro = 
    weap_pro =
    armor_pro = 
    skill_pro_num = 
    skill_pro_choice = 
    
class damage_type:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    source = 

class dice:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    value = db.Column(db.Integer)
    roller = 

class weapon:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    damage = 
    num_of_dice = db.Column(db.Integer)
    dmg_type = 
    properties =
    tech_level = db.Column(db.Integer)
    ranged = db.Column(db.Boolean)
    reach = db.Column(db.Integer)
    normal_range = db.Column(db.Integer)
    long_range = db.Column(db.Integer)
    martial = db.Column(db.Boolean)
    wielder =

class armor:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    armor_size = db.Column(db.String(64))
    ac = db.Column(db.Integer)
    ac_mod_type =
    ac_mod_max = db.Column(db.Integer)
    str_req = db.Column(db.Integer)
    stealth = db.Column(db.String(64))
    wearer =

class gear:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    owner =

class 

