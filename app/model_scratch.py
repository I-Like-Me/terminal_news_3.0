
# class Character(db.Model):
#     ladder =
#     background =
#     alignment =
#     pro_abilities = 
#     pro_skills =
#     weapons = #class weapon(db.Model):
#     armor = #class armor(db.Model):
#     gear =
#     factions = 
#     parties = #class party(db.Model):
#     prepd_spells =
#     spellbook =
#     feats =


# class char_personal_info(db.Model):
#     cur_race =
#     birth_race =
#     birth_loc = 
#     cur_loc = 
#     job = 

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

# class Features(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     level_access = db.Column(db.Integer)
#     description = db.Column(db.String(200))
#     feature_class = #class cls_5e(db.Model):
#     feature_arch = #class architype(db.Model):

# class gear(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     gear_trained_classes = #class cls_5e(db.Model):
#     owner = #class Character(db.Model):


