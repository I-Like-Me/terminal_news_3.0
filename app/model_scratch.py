
# class Character(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     player = #class User(db.Model):
#     level = db.Column(db.Integer)
#     npc = db.Column(db.Boolean)
#     cls = #class cls_5e(db.Model):
#     knows_cls = #class knows_char_cls_arch(db.Model):
#     ladder =
#     background =
#     proficiency = db.Column(db.Integer)
#     speed = db.Column(db.Integer)
#     passive_perc = db.Column(db.Integer)
#     armor_class = db.Column(db.Integer)
#     inspiration = db.Column(db.Boolean)
#     initiative = db.Column(db.Integer)
#     alignment =
#     cur_hit_points = db.Column(db.Integer)
#     temp_hit_points = db.Column(db.Integer)
#     ability_numbers = #class char_ability_scores(db.Model):
#     pro_abilities = 
#     skill_numbers = #class char_skill_scores(db.Model):
#     pro_skills =
#     personal_info = #class char_personal_info(db.Model):
#     weapons = #class weapon(db.Model):
#     armor = #class armor(db.Model):
#     gear =
#     factions = 
#     parties = #class party(db.Model):
#     admin = db.Column(db.Boolean)
#     backpack = db.Column(db.String(5000))
#     prepd_spells =
#     spellbook =
#     feats =
#     play_notes = db.Column(db.String(5000))

# class char_personal_info(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     knows_name = #class knows_char_cur_name(db.Model):
#     birth_name = db.Column(db.String(64))
#     self_k_b_name = db.Column(db.Boolean)
#     knows_birth_name = #class knows_char_birth_name(db.Model):
#     real_age = db.Column(db.Integer)
#     knows_r_age = #class knows_char_real_age(db.Model):
#     self_k_r_age = db.Column(db.Boolean)
#     fake_age = db.Column(db.Integer)
#     knows_f_age = #class knows_char_fake_age(db.Model):
#     cur_race =
#     knows_c_race = #class knows_char_cur_race(db.Model):
#     birth_race =
#     self_k_b_race = db.Column(db.Boolean)
#     knows_b_race = #class knows_char_birth_race(db.Model):
#     birth_loc = 
#     knows_b_loc = #class knows_char_birth_loc(db.Model):
#     self_k_b_loc = db.Column(db.Boolean)
#     cur_loc = 
#     knows_c_loc = #class knows_char_cur_loc(db.Model):
#     job = 
#     knows_c_job = #class knows_char_job(db.Model):
#     history = db.Column(db.String(5000))
#     info_subject = #class Character(db.Model):

# class char_skill_scores(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     acrobatics = db.Column(db.Integer)
#     animal_handling = db.Column(db.Integer)
#     arcana = db.Column(db.Integer)
#     athletics = db.Column(db.Integer)
#     computer_use = db.Column(db.Integer)
#     deception = db.Column(db.Integer)
#     demolitions = db.Column(db.Integer)
#     engineering = db.Column(db.Integer)
#     history = db.Column(db.Integer)
#     insight = db.Column(db.Integer)
#     intimidation = db.Column(db.Integer)
#     investigation = db.Column(db.Integer)
#     medicine = db.Column(db.Integer)
#     nature = db.Column(db.Integer)
#     perception = db.Column(db.Integer)
#     performance = db.Column(db.Integer)
#     persuasion = db.Column(db.Integer)
#     religion = db.Column(db.Integer)
#     sciences = db.Column(db.Integer)
#     sleight_of_hand = db.Column(db.Integer)
#     stealth = db.Column(db.Integer)
#     survival = db.Column(db.Integer)
#     skilled_char = #class Character(db.Model):

# class char_ability_scores(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     strength = db.Column(db.Integer)
#     dexterity = db.Column(db.Integer)
#     constitution = db.Column(db.Integer)
#     intelligence = db.Column(db.Integer)
#     wisdom = db.Column(db.Integer)
#     charisma = db.Column(db.Integer)
#     able_char = #class Character(db.Model):

# class party(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     members = #class Character(db.Model):
#     max_members = db.Column(db.Integer)
#     joined_game = 

# class cls_5e(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     arch = db.Column(db.String(64))
#     arch_choices = #class architype(db.Model):
#     cls_features = #class cls_features(db.Model):
#     total_hit_dice = db.Column(db.String(64))
#     cur_hit_dice = db.Column(db.String(64))
#     hit_dice_type = 
#     hit_pnt_l01 = db.Column(db.Integer)
#     sav_throw = 
#     tool_pro = #class gear(db.Model):
#     weap_pro = #class weapon(db.Model):
#     armor_pro = #class armor(db.Model):
#     skill_pro_choice = 
#     max_num_pro_skills = db.Column(db.Integer)
#     classed_char = #class Character(db.Model):

# class architype(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     arch = #arch_features(db.Model):
#     arched_class = #class cls_5e(db.Model):

# class knows_char_cls_arch(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     cls_arch_holder = #class Character(db.Model):

# class knows_char_real_age(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     real_aged_char = #class char_personal_info(db.Model):

# class knows_char_fake_age(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     fake_aged_char = #class char_personal_info(db.Model):

# class knows_char_cur_name(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     cur_named_char = #class char_personal_info(db.Model):

# class knows_char_birth_name(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     birth_named_char = #class char_personal_info(db.Model):

# class knows_char_birth_race(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     birth_race_char = #class char_personal_info(db.Model):

# class knows_char_cur_race(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     cur_race_char = #class char_personal_info(db.Model):

# class knows_char_birth_loc(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     birth_loc_char = #class char_personal_info(db.Model):

# class knows_char_cur_loc(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     cur_loc_char = #class char_personal_info(db.Model):

# class knows_char_job(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     employed_char = #class char_personal_info(db.Model):

# class cls_features(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     level_access = db.Column(db.Integer)
#     description = db.Column(db.String(200))
#     feature_class = #class cls_5e(db.Model):

# class arch_features(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     level_access = db.Column(db.Integer)
#     description = db.Column(db.String(200))
#     feature_arch = #class architype(db.Model):

# class damage_type(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     source = 

# class dice(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     value = db.Column(db.Integer)
#     roller = 

# class weapon(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     damage = 
#     num_of_dice = db.Column(db.Integer)
#     dmg_type = 
#     properties =
#     tech_level = db.Column(db.Integer)
#     ranged = db.Column(db.Boolean)
#     reach = db.Column(db.Integer)
#     normal_range = db.Column(db.Integer)
#     long_range = db.Column(db.Integer)
#     martial = db.Column(db.Boolean)
#     weap_trained_classes = #class cls_5e(db.Model):
#     wielder = #class Character(db.Model):

# class armor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     armor_size = db.Column(db.String(64))
#     ac = db.Column(db.Integer)
#     ac_mod_type =
#     ac_mod_max = db.Column(db.Integer)
#     str_req = db.Column(db.Integer)
#     stealth = db.Column(db.String(64))
#     armor_trained_classes = #class cls_5e(db.Model):
#     wearer = #class Character(db.Model):

# class gear(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     gear_trained_classes = #class cls_5e(db.Model):
#     owner = #class Character(db.Model):


