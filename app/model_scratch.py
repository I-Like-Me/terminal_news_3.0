
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

# class architype(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     arch = #arch_features(db.Model):
#     arched_class = #class cls_5e(db.Model):

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


