from app import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.dialects.postgresql import JSONB, insert

user_char_table = db.Table(
    "user_char_table",
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
)

weap_dice_table = db.Table(
    "weap_dice_table",
    db.Column("weapon_id", db.ForeignKey("weapon.id"), primary_key=True),
    db.Column("dice_id", db.ForeignKey("dice.id"), primary_key=True),
)

weap_dmg_type_table = db.Table(
    "weap_dmg_type_table",
    db.Column("weapon_id", db.ForeignKey("weapon.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

cls_arch_table = db.Table(
    "cls_arch_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("architype_id", db.ForeignKey("architype.id"), primary_key=True),
)

cls_feature_table = db.Table(
    "cls_feature_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("feature_id", db.ForeignKey("feature.id"), primary_key=True),
)

arch_feature_table = db.Table(
    "arch_feature_table",
    db.Column("architype_id", db.ForeignKey("architype.id"), primary_key=True),
    db.Column("feature_id", db.ForeignKey("feature.id"), primary_key=True),
)

cls_hit_dice_table = db.Table(
    "cls_hit_dice_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("dice_id", db.ForeignKey("dice.id"), primary_key=True),
)

cls_sav_ability_table = db.Table(
    "cls_sav_ability_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("ability_id", db.ForeignKey("ability.id"), primary_key=True),
)

cls_pro_skill_table = db.Table(
    "cls_pro_skill_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("skill_id", db.ForeignKey("skill.id"), primary_key=True),
)

cls_pro_tool_table = db.Table(
    "cls_pro_tool_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("gear_id", db.ForeignKey("gear.id"), primary_key=True),
)

cls_pro_weap_table = db.Table(
    "cls_pro_weap_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("weapon_id", db.ForeignKey("weapon.id"), primary_key=True),
)

cls_pro_armor_table = db.Table(
    "cls_pro_armor_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
)

weapon_property_table = db.Table(
    "weapon_property_table",
    db.Column("weapon_id", db.ForeignKey("weapon.id"), primary_key=True),
    db.Column("property_id", db.ForeignKey("property.id"), primary_key=True),
)

armor_property_table = db.Table(
    "armor_property_table",
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
    db.Column("property_id", db.ForeignKey("property.id"), primary_key=True),
)

vehicle_property_table = db.Table(
    "vehicle_property_table",
    db.Column("vehicle_id", db.ForeignKey("vehicle.id"), primary_key=True),
    db.Column("property_id", db.ForeignKey("property.id"), primary_key=True),
)

mech_property_table = db.Table(
    "mech_property_table",
    db.Column("mech_id", db.ForeignKey("mech.id"), primary_key=True),
    db.Column("property_id", db.ForeignKey("property.id"), primary_key=True),
)

cyber_property_table = db.Table(
    "cyber_property_table",
    db.Column("cybernetic_id", db.ForeignKey("cybernetic.id"), primary_key=True),
    db.Column("property_id", db.ForeignKey("property.id"), primary_key=True),
)

user_game_table = db.Table(
    "user_game_table",
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("game_id", db.ForeignKey("game.id"), primary_key=True),
)

char_party_table = db.Table(
    "char_party_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("party_id", db.ForeignKey("party.id"), primary_key=True),
)

game_party_table = db.Table(
    "game_party_table",
    db.Column("game_id", db.ForeignKey("game.id"), primary_key=True),
    db.Column("party_id", db.ForeignKey("party.id"), primary_key=True),
)

game_npc_pool_table = db.Table(
    "game_npc_pool_table",
    db.Column("game_id", db.ForeignKey("game.id"), primary_key=True),
    db.Column("npcpool_id", db.ForeignKey("npcpool.id"), primary_key=True),
)

char_npc_pool_table = db.Table(
    "char_npc_pool_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("npcpool_id", db.ForeignKey("npcpool.id"), primary_key=True),
)

char_ladder_table = db.Table(
    "char_ladder_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("ladder_id", db.ForeignKey("ladder.id"), primary_key=True),
)

ladder_feature_table = db.Table(
    "ladder_feature_table",
    db.Column("ladder_id", db.ForeignKey("ladder.id"), primary_key=True),
    db.Column("feature_id", db.ForeignKey("feature.id"), primary_key=True),
)

char_background_table = db.Table(
    "char_background_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("feature_id", db.ForeignKey("background.id"), primary_key=True),
)

char_alignment_table = db.Table(
    "char_alignment_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("alignment_id", db.ForeignKey("alignment.id"), primary_key=True),
)

char_faction_table = db.Table(
    "char_faction_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("faction_id", db.ForeignKey("faction.id"), primary_key=True),
)

char_pro_skill_table = db.Table(
    "char_pro_skill_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("skill_id", db.ForeignKey("skill.id"), primary_key=True),
)

char_weap_table = db.Table(
    "char_weap_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("weapon_id", db.ForeignKey("weapon.id"), primary_key=True),
)

ability_armor_mod_table = db.Table(
    "ability_armor_mod_table",
    db.Column("ability_id", db.ForeignKey("ability.id"), primary_key=True),
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
)

char_armor_table = db.Table(
    "char_armor_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
)

char_gear_table = db.Table(
    "char_gear_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("gear_id", db.ForeignKey("gear.id"), primary_key=True),
)

race_feature_table = db.Table(
    "race_feature_table",
    db.Column("race_id", db.ForeignKey("race.id"), primary_key=True),
    db.Column("feature_id", db.ForeignKey("feature.id"), primary_key=True),
)

life_info_cur_race_table = db.Table(
    "life_info_cur_race_table",
    db.Column("lifeinfo_id", db.ForeignKey("lifeinfo.id"), primary_key=True),
    db.Column("race_id", db.ForeignKey("race.id"), primary_key=True),
)

life_info_birth_race_table = db.Table(
    "life_info_birth_race_table",
    db.Column("lifeinfo_id", db.ForeignKey("lifeinfo.id"), primary_key=True),
    db.Column("race_id", db.ForeignKey("race.id"), primary_key=True),
)

life_info_cur_loc_table = db.Table(
    "life_info_cur_loc_table",
    db.Column("lifeinfo_id", db.ForeignKey("lifeinfo.id"), primary_key=True),
    db.Column("location_id", db.ForeignKey("location.id"), primary_key=True),
)

life_info_birth_loc_table = db.Table(
    "life_info_birth_loc_table",
    db.Column("lifeinfo_id", db.ForeignKey("lifeinfo.id"), primary_key=True),
    db.Column("location_id", db.ForeignKey("location.id"), primary_key=True),
)

cls_info_arch_table = db.Table(
    "cls_info_arch_table",
    db.Column("clsinfo_id", db.ForeignKey("clsinfo.id"), primary_key=True),
    db.Column("architype_id", db.ForeignKey("architype.id"), primary_key=True),
)

race_dmg_resist_table = db.Table(
    "race_dmg_resist_table",
    db.Column("race_id", db.ForeignKey("race.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

race_dmg_immune_table = db.Table(
    "race_dmg_immune_table",
    db.Column("race_id", db.ForeignKey("race.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

race_dmg_vulner_table = db.Table(
    "race_dmg_vulner_table",
    db.Column("race_id", db.ForeignKey("race.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

cls_dmg_resist_table = db.Table(
    "cls_dmg_resist_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

cls_dmg_immune_table = db.Table(
    "cls_dmg_immune_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

cls_dmg_vulner_table = db.Table(
    "cls_dmg_vulner_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

feature_dmg_resist_table = db.Table(
    "feature_dmg_resist_table",
    db.Column("feature_id", db.ForeignKey("feature.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

feature_dmg_immune_table = db.Table(
    "feature_dmg_immune_table",
    db.Column("feature_id", db.ForeignKey("feature.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

feature_dmg_vulner_table = db.Table(
    "feature_dmg_vulner_table",
    db.Column("feature_id", db.ForeignKey("feature.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

armor_dmg_resist_table = db.Table(
    "armor_dmg_resist_table",
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

armor_dmg_immune_table = db.Table(
    "armor_dmg_immune_table",
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

armor_dmg_vulner_table = db.Table(
    "armor_dmg_vulner_table",
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

cls_spell_table = db.Table(
    "cls_spell_table",
    db.Column("cls_5e_id", db.ForeignKey("cls_5e.id"), primary_key=True),
    db.Column("spell_id", db.ForeignKey("spell.id"), primary_key=True),
)

char_spell_table = db.Table(
    "char_spell_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("spell_id", db.ForeignKey("spell.id"), primary_key=True),
)

char_vehicle_table = db.Table(
    "char_vehicle_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("vehicle_id", db.ForeignKey("vehicle.id"), primary_key=True),
)

char_feat_table = db.Table(
    "char_feat_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("feat_id", db.ForeignKey("feat.id"), primary_key=True),
)

char_mech_table = db.Table(
    "char_mech_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("mech_id", db.ForeignKey("mech.id"), primary_key=True),
)

char_cyber_table = db.Table(
    "char_cyber_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("cybernetic_id", db.ForeignKey("cybernetic.id"), primary_key=True),
)

char_cls_info_table = db.Table(
    "char_cls_info_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("clsinfo_id", db.ForeignKey("clsinfo.id"), primary_key=True),
)

ammo_power_dmg_type_table = db.Table(
    "ammo_power_dmg_type_table",
    db.Column("ammo_power_id", db.ForeignKey("ammo_power.id"), primary_key=True),
    db.Column("damagetype_id", db.ForeignKey("damagetype.id"), primary_key=True),
)

ammo_power_weap_table = db.Table(
    "ammo_power_weap_table",
    db.Column("ammo_power_id", db.ForeignKey("ammo_power.id"), primary_key=True),
    db.Column("weapon_id", db.ForeignKey("weapon.id"), primary_key=True),
)

ammo_power_armor_table = db.Table(
    "ammo_power_armor_table",
    db.Column("ammo_power_id", db.ForeignKey("ammo_power.id"), primary_key=True),
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
)

ammo_power_gear_table = db.Table(
    "ammo_power_gear_table",
    db.Column("ammo_power_id", db.ForeignKey("ammo_power.id"), primary_key=True),
    db.Column("gear_id", db.ForeignKey("gear.id"), primary_key=True),
)

ammo_power_vehicle_table = db.Table(
    "ammo_power_vehicle_table",
    db.Column("ammo_power_id", db.ForeignKey("ammo_power.id"), primary_key=True),
    db.Column("vehicle_id", db.ForeignKey("vehicle.id"), primary_key=True),
)

ammo_power_mech_table = db.Table(
    "ammo_power_mech_table",
    db.Column("ammo_power_id", db.ForeignKey("ammo_power.id"), primary_key=True),
    db.Column("mech_id", db.ForeignKey("mech.id"), primary_key=True),
)

fac_rank_table = db.Table(
    "fac_rank_table",
    db.Column("faction_id", db.ForeignKey("faction.id"), primary_key=True),
    db.Column("rank_id", db.ForeignKey("rank.id"), primary_key=True),
)

char_rank_table = db.Table(
    "char_rank_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("rank_id", db.ForeignKey("rank.id"), primary_key=True),
)

class CharCls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_cls = db.Column(db.String(64), index=True, unique=True)
    character_id = db.Column("character_id", db.Integer, db.ForeignKey("character.id"))
    cls_5e_id = db.Column("cls_5e_id", db.Integer, db.ForeignKey("cls_5e.id"))
    cls_level = db.Column(db.Integer)

    classed_character = db.relationship("Character", back_populates='cls_association')
    cls = db.relationship("Cls_5e", back_populates='classed_character_association')
   
    def __repr__(self):
        return f'<CharCls {self.char_cls}>'
    
# class CharKnow(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     char_char = db.Column(db.String(64), index=True, unique=True)
#     learner_id = db.Column("learner_id", db.Integer, db.ForeignKey("character.id"))
#     subject_id = db.Column("subject_id", db.Integer, db.ForeignKey("character.id"))
#     topics = db.Column(JSONB)

#     learner_char = db.relationship("Character", back_populates='subject_association')
#     subject_char = db.relationship("Character", back_populates='learner_association')
   
#     def __repr__(self):
#         return f'<CharKnow {self.char_char}>'

class CharKnow(db.Model):
    __tablename__ = 'char_know'
    id = db.Column(db.Integer, primary_key=True)
    char_char = db.Column(db.String(64), index=True, unique=True)
    learner_id = db.Column("learner_id", db.Integer, db.ForeignKey("character.id"))
    subject_id = db.Column("subject_id", db.Integer, db.ForeignKey("character.id"))
    topics = db.Column(JSONB)

    learner_char = db.relationship("Character", foreign_keys=[learner_id])
    subject_char = db.relationship("Character", foreign_keys=[subject_id])
   
    def __repr__(self):
        return f'<CharKnow {self.char_char}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    character = db.relationship("Character", secondary=user_char_table, back_populates="player")
    games = db.relationship("Game", secondary=user_game_table, back_populates="gm")
    admin = db.Column(db.Boolean)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def claim_char(self, char_pick):
        if char_pick.npc != True and len(char_pick.player) == 0:
            self.character.append(char_pick)

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    player = db.relationship("User", secondary=user_char_table, back_populates="character")
    parties = db.relationship("Party", secondary=char_party_table, back_populates="members")
    proficiency = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    passive_perc = db.Column(db.Integer)
    armor_class = db.Column(db.Integer)
    inspiration = db.Column(db.Boolean)
    initiative = db.Column(db.Integer)
    cur_hit_points = db.Column(db.Integer)
    temp_hit_points = db.Column(db.Integer)
    level = db.Column(db.Integer, default=0)
    ladder = db.relationship("Ladder", secondary=char_ladder_table, back_populates="char_ladder")
    background = db.relationship("Background", secondary=char_background_table, back_populates="char_bg")
    alignment = db.relationship("Alignment", secondary=char_alignment_table, back_populates="aligned_char")
    factions = db.relationship("Faction", secondary=char_faction_table, back_populates="char_fac")
    ranks = db.relationship("Rank", secondary=char_rank_table, back_populates="ranked_char")
    ability_numbers = db.relationship("AbilityScores")
    pro_skills = db.relationship("Skill", secondary=char_pro_skill_table, back_populates="skl_trained_char")
    skill_numbers = db.relationship("SkillScores")
    cls_association = db.relationship("CharCls", back_populates="classed_character")
    classes = association_proxy("cls_association", "cls")
    life_info = db.relationship("Lifeinfo")
    cls_info_sheets = db.relationship("Clsinfo", secondary=char_cls_info_table, back_populates="cls_info_holder") 
    weapons = db.relationship("Weapon", secondary=char_weap_table, back_populates="wielder")
    armor = db.relationship("Armor", secondary=char_armor_table, back_populates="wearer")
    gear = db.relationship("Gear", secondary=char_gear_table, back_populates="owner")
    vehicle = db.relationship("Vehicle", secondary=char_vehicle_table, back_populates="owner")
    mech = db.relationship("Mech", secondary=char_mech_table, back_populates="owner")
    cybernetics = db.relationship("Cybernetic", secondary=char_cyber_table, back_populates="owner")
    prepped_spells = db.relationship("Spell", secondary=char_spell_table, back_populates="spell_prepper") 
    feats = db.relationship("Feat", secondary=char_feat_table, back_populates="char_feat")
    backpack = db.Column(db.String(5000))
    play_notes = db.Column(db.String(5000))
    npc = db.Column(db.Boolean)
    npc_group = db.relationship("Npcpool", secondary=char_npc_pool_table, back_populates="picked_npc")
    
    knows = db.relationship(
        'Character',
        secondary='char_know',
        primaryjoin=id == CharKnow.learner_id,
        secondaryjoin=id == CharKnow.subject_id,
        backref='topic_check'
    )

    # subject_association = db.relationship("CharKnow", back_populates="learner_char")
    # subjects = association_proxy("subject_association", "subject_char")

    # learner_association = db.relationship("CharKnow", back_populates="subject_char")
    # learners = association_proxy('learner_association', 'learner_char')

    def __repr__(self):
        return f'<Character {self.name}>'

    def pick_cls(self, cls_pick):
        char_cls_ready = CharCls(classed_character=self, cls=cls_pick, cls_level=1, char_cls=f'{self.name[:3]}{self.id}_{cls_pick.name[:3]}{cls_pick.id}')
        self.level += 1
        db.session.add(char_cls_ready)
        db.session.commit()

    def lvl_up_cls(self, cls_target):
        for cls in self.classes:
            if cls.name == cls_target:
                char_cls_entry = CharCls.query.filter_by(char_cls=f'{self.name[:3]}{self.id}_{cls.name[:3]}{cls.id}').first()
                char_cls_entry.cls_level += 1
                self.level += 1
        db.session.commit()
    
    def get_cls_lvl(self, cls_target):
        for cls in self.classes:
            if cls.name == cls_target:
                char_cls_entry = CharCls.query.filter_by(char_cls=f'{self.name[:3]}{self.id}_{cls.name[:3]}{cls.id}').first()
                return char_cls_entry.cls_level      

class Cls_5e(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    classed_character_association = db.relationship("CharCls", back_populates="cls")
    classed_characters = association_proxy('classed_character_association', 'classed_character')
    arch_choices = db.relationship("Architype", secondary=cls_arch_table, back_populates="arched_cls")
    cls_features = db.relationship("Feature", secondary=cls_feature_table, back_populates="featured_cls")
    hit_dice_type = db.relationship("Dice", secondary=cls_hit_dice_table, back_populates="cls_hit_dice")
    sav_throws = db.relationship("Ability", secondary=cls_sav_ability_table, back_populates="cls_sav_throw")
    tool_pros = db.relationship("Gear", secondary=cls_pro_tool_table, back_populates="tool_trained_cls")
    weap_pros = db.relationship("Weapon", secondary=cls_pro_weap_table, back_populates="weap_trained_cls")
    armor_pros = db.relationship("Armor", secondary=cls_pro_armor_table, back_populates="armor_trained_cls") 
    skill_pro_choice = db.relationship("Skill", secondary=cls_pro_skill_table, back_populates="skl_trained_cls")
    max_num_pro_skills = db.Column(db.Integer)
    dmg_resist = db.relationship("Damagetype", secondary=cls_dmg_resist_table, back_populates="cls_resist")
    dmg_immune = db.relationship("Damagetype", secondary=cls_dmg_immune_table, back_populates="cls_immune")
    dmg_vulner = db.relationship("Damagetype", secondary=cls_dmg_vulner_table, back_populates="cls_vulner")    
    spellbook = db.relationship("Spell", secondary=cls_spell_table, back_populates="cls_books") 

    def __repr__(self):
        return f'<Cls_5e {self.name}>'

    def new_cls_adder(cls_name):
        new_cls = Cls_5e(name=cls_name)
        db.session.add(new_cls)
        db.session.commit()

class Ladder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    char_ladder = db.relationship("Character", secondary=char_ladder_table, back_populates="ladder")
    ladder_features = db.relationship("Feature", secondary=ladder_feature_table, back_populates="featured_ladder")
    ladder_gain_5 = db.Column(db.String(64))
    ladder_gain_11 = db.Column(db.String(64))
    ladder_gain_17 = db.Column(db.String(64))

    def __repr__(self):
        return f'<Ladder {self.name}>'

    def new_ladder_adder(ladder_name):
        new_ladder = Ladder(name=ladder_name)
        db.session.add(new_ladder)
        db.session.commit()

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    race_features = db.relationship("Feature", secondary=race_feature_table, back_populates="featured_race")
    char_cur_race = db.relationship("Lifeinfo", secondary=life_info_cur_race_table, back_populates="cur_race")
    char_birth_race = db.relationship("Lifeinfo", secondary=life_info_birth_race_table, back_populates="birth_race")
    dmg_resist = db.relationship("Damagetype", secondary=race_dmg_resist_table, back_populates="race_resist")
    dmg_immune = db.relationship("Damagetype", secondary=race_dmg_immune_table, back_populates="race_immune")
    dmg_vulner = db.relationship("Damagetype", secondary=race_dmg_vulner_table, back_populates="race_vulner")

    def __repr__(self):
        return f'<Race {self.name}>'

    def new_race_adder(race_name):
        new_race = Race(name=race_name)
        db.session.add(new_race)
        db.session.commit()

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(1000))
    char_cur_loc = db.relationship("Lifeinfo", secondary=life_info_cur_loc_table, back_populates="cur_loc")
    char_birth_loc = db.relationship("Lifeinfo", secondary=life_info_birth_loc_table, back_populates="birth_loc")

    def __repr__(self):
        return f'<Location {self.name}>'

    def new_loc_adder(loc_name):
        new_loc = Location(name=loc_name)
        db.session.add(new_loc)
        db.session.commit()

class Background(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    char_bg = db.relationship("Character", secondary=char_background_table, back_populates="background")

    def __repr__(self):
        return f'<Background {self.name}>'

    def new_bg_adder(bg_name):
        new_bg = Background(name=bg_name)
        db.session.add(new_bg)
        db.session.commit()

class Alignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    aligned_char = db.relationship("Character", secondary=char_alignment_table, back_populates="alignment")

    def __repr__(self):
        return f'<Alignment {self.name}>'

    def new_align_adder(align_name):
        new_align = Alignment(name=align_name)
        db.session.add(new_align)
        db.session.commit()

class Faction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    char_fac = db.relationship("Character", secondary=char_faction_table, back_populates="factions")
    fac_ranks = db.relationship("Rank", secondary=fac_rank_table, back_populates="ranked_facs")

    def __repr__(self):
        return f'<Faction {self.name}>'

    def new_fac_adder(fac_name):
        new_fac = Faction(name=fac_name)
        db.session.add(new_fac)
        db.session.commit()

class Rank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    ranked_facs = db.relationship("Faction", secondary=fac_rank_table, back_populates="fac_ranks")
    ranked_char = db.relationship("Character", secondary=char_rank_table, back_populates="ranks")

    def __repr__(self):
        return f'<Rank {self.name}>'

    def new_rank_adder(rank_name):
        new_rank = Rank(name=rank_name)
        db.session.add(new_rank)
        db.session.commit()
        
class Architype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    arch_features = db.relationship("Feature", secondary=arch_feature_table, back_populates="featured_arch")
    arched_cls = db.relationship("Cls_5e", secondary=cls_arch_table, back_populates="arch_choices")
    picked_arch = db.relationship("Clsinfo", secondary=cls_info_arch_table, back_populates="archs")

    def __repr__(self):
        return f'<Architype {self.name}>'

    def new_arch_adder(arch_name):
        new_arch = Architype(name=arch_name)
        db.session.add(new_arch)
        db.session.commit()

class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    level_access = db.Column(db.Integer)
    description = db.Column(db.String(200))
    featured_cls = db.relationship("Cls_5e", secondary=cls_feature_table, back_populates="cls_features")
    featured_arch = db.relationship("Architype", secondary=arch_feature_table, back_populates="arch_features")
    featured_ladder = db.relationship("Ladder", secondary=ladder_feature_table, back_populates="ladder_features")
    featured_race = db.relationship("Race", secondary=race_feature_table, back_populates="race_features")
    dmg_resist = db.relationship("Damagetype", secondary=feature_dmg_resist_table, back_populates="feature_resist")
    dmg_immune = db.relationship("Damagetype", secondary=feature_dmg_immune_table, back_populates="feature_immune")
    dmg_vulner = db.relationship("Damagetype", secondary=feature_dmg_vulner_table, back_populates="feature_vulner")

    def __repr__(self):
        return f'<Feature {self.name}>'

class Ability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    cls_sav_throw = db.relationship("Cls_5e", secondary=cls_sav_ability_table, back_populates="sav_throws")
    armor_mod = db.relationship("Armor", secondary=ability_armor_mod_table, back_populates="ac_mod_type")

    def __repr__(self):
        return f'<Ability {self.name}>'

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    skl_trained_cls = db.relationship("Cls_5e", secondary=cls_pro_skill_table, back_populates="skill_pro_choice")
    skl_trained_char = db.relationship("Character", secondary=char_pro_skill_table, back_populates="pro_skills")

    def __repr__(self):
        return f'<Skill {self.name}>'

class Feat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    char_feat = db.relationship("Character", secondary=char_feat_table, back_populates="feats")

    def __repr__(self):
        return f'<Feat {self.name}>' 

class Lifeinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(64), index=True, unique=True)
    birth_name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    real_age  = db.Column(db.Integer)
    cur_race = db.relationship("Race", secondary=life_info_cur_race_table, back_populates="char_cur_race")
    birth_race = db.relationship("Race", secondary=life_info_birth_race_table, back_populates="char_birth_race")
    cur_loc = db.relationship("Location", secondary=life_info_cur_loc_table, back_populates="char_cur_loc")
    birth_loc = db.relationship("Location", secondary=life_info_birth_loc_table, back_populates="char_birth_loc")
    public_history = db.Column(db.String(5000))
    learned_history = db.Column(db.String(5000))
    hidden_history = db.Column(db.String(5000))
    life_info_holder = db.Column(db.Integer, db.ForeignKey("character.id"))

    def __repr__(self):
        return f'<Lifeinfo {self.char_name}>'

class Clsinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_cls_info_name = db.Column(db.String(64), index=True, unique=True)
    archs = db.relationship("Architype", secondary=cls_info_arch_table, back_populates="picked_arch")
    total_hit_dice = db.Column(db.String(64))
    cur_hit_dice = db.Column(db.String(64))
    cls_info_holder = db.relationship("Character", secondary=char_cls_info_table, back_populates="cls_info_sheets")

    def __repr__(self):
        return f'<Clsinfo {self.char_cls_info_name}>'

class SkillScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(64), index=True, unique=True)
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
    skilled_char = db.Column(db.Integer, db.ForeignKey("character.id")) 

    def __repr__(self):
        return f'<SkillScores {self.char_name}>'
    
class AbilityScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(64), index=True, unique=True)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    able_char = db.Column(db.Integer, db.ForeignKey("character.id"))

    def __repr__(self):
        return f'<AbilityScores {self.char_name}>'

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    damage_dice = db.relationship("Dice", secondary=weap_dice_table, back_populates="damage_roller")
    num_of_dice = db.Column(db.Integer)
    dmg_type = db.relationship("Damagetype", secondary=weap_dmg_type_table, back_populates="weap_source")
    properties = db.relationship("Property", secondary=weapon_property_table, back_populates="weap_prop")
    tech_level = db.Column(db.Integer)
    ranged = db.Column(db.Boolean)
    reach = db.Column(db.Integer)
    normal_range = db.Column(db.Integer)
    long_range = db.Column(db.Integer)
    ammo = db.relationship("Ammo_power", secondary=ammo_power_weap_table, back_populates="weap_load")
    weap_trained_cls = db.relationship("Cls_5e", secondary=cls_pro_weap_table, back_populates="weap_pros")
    wielder = db.relationship("Character", secondary=char_weap_table, back_populates="weapons")

    def __repr__(self):
        return f'<Weapon {self.name}>'

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    weap_prop = db.relationship("Weapon", secondary=weapon_property_table, back_populates="properties")
    armor_prop = db.relationship("Armor", secondary=armor_property_table, back_populates="properties")
    vehicle_prop = db.relationship("Vehicle", secondary=vehicle_property_table, back_populates="properties")
    mech_prop = db.relationship("Mech", secondary=mech_property_table, back_populates="properties")
    cyber_prop = db.relationship("Cybernetic", secondary=cyber_property_table, back_populates="properties")

    def __repr__(self):
        return f'<Property {self.name}>'

class Ammo_power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    tech_level = db.Column(db.Integer)
    dmg_type = db.relationship("Damagetype", secondary=ammo_power_dmg_type_table, back_populates="ammo_source")
    weap_load = db.relationship("Weapon", secondary=ammo_power_weap_table, back_populates="ammo")
    armor_load = db.relationship("Armor", secondary=ammo_power_armor_table, back_populates="power")
    gear_load  = db.relationship("Gear", secondary=ammo_power_gear_table, back_populates="power")
    vehicle_load = db.relationship("Vehicle", secondary=ammo_power_vehicle_table, back_populates="power")
    mech_load = db.relationship("Mech", secondary=ammo_power_mech_table, back_populates="power")

    def __repr__(self):
        return f'<Ammo {self.name}>' 

class Armor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    armor_size = db.Column(db.String(64))
    ac = db.Column(db.Integer)
    ac_mod_type = db.relationship("Ability", secondary=ability_armor_mod_table, back_populates="armor_mod")
    ac_mod_max = db.Column(db.Integer)
    str_req = db.Column(db.Integer)
    stealth = db.Column(db.String(64))
    dmg_resist = db.relationship("Damagetype", secondary=armor_dmg_resist_table, back_populates="armor_resist")
    dmg_immune = db.relationship("Damagetype", secondary=armor_dmg_immune_table, back_populates="armor_immune")
    dmg_vulner = db.relationship("Damagetype", secondary=armor_dmg_vulner_table, back_populates="armor_vulner")
    tech_level = db.Column(db.Integer)
    power = db.relationship("Ammo_power", secondary=ammo_power_armor_table, back_populates="armor_load")
    properties = db.relationship("Property", secondary=armor_property_table, back_populates="armor_prop")
    armor_trained_cls = db.relationship("Cls_5e", secondary=cls_pro_armor_table, back_populates="armor_pros") 
    wearer = db.relationship("Character", secondary=char_armor_table, back_populates="armor")

    def __repr__(self):
        return f'<Armor {self.name}>'

class Gear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    tech_level = db.Column(db.Integer)
    power = db.relationship("Ammo_power", secondary=ammo_power_gear_table, back_populates="gear_load")
    tool_trained_cls = db.relationship("Cls_5e", secondary=cls_pro_tool_table, back_populates="tool_pros")
    owner = db.relationship("Character", secondary=char_gear_table, back_populates="gear")
    
    def __repr__(self):
        return f'<Gear {self.name}>'

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    type = db.Column(db.String(12))
    speed = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    power = db.relationship("Ammo_power", secondary=ammo_power_vehicle_table, back_populates="vehicle_load")
    tech_level = db.Column(db.Integer)
    properties = db.relationship("Property", secondary=vehicle_property_table, back_populates="vehicle_prop")
    owner = db.relationship("Character", secondary=char_vehicle_table, back_populates="vehicle")
    
    def __repr__(self):
        return f'<Vehicle {self.name}>'

class Mech(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    power = db.relationship("Ammo_power", secondary=ammo_power_mech_table, back_populates="mech_load")
    tech_level = db.Column(db.Integer)
    properties = db.relationship("Property", secondary=mech_property_table, back_populates="mech_prop")
    owner = db.relationship("Character", secondary=char_mech_table, back_populates="mech")
    
    def __repr__(self):
        return f'Mech {self.name}>'

class Cybernetic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    body_part = db.Column(db.String(12))
    tech_level = db.Column(db.Integer)
    properties = db.relationship("Property", secondary=cyber_property_table, back_populates="cyber_prop")
    owner = db.relationship("Character", secondary=char_cyber_table, back_populates="cybernetics")
    
    def __repr__(self):
        return f'Mech {self.name}>'

class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    level = db.Column(db.Integer, default=1)
    cls_books = db.relationship("Cls_5e", secondary=cls_spell_table, back_populates="spellbook") 
    spell_prepper = db.relationship("Character", secondary=char_spell_table, back_populates="prepped_spells") 

    def __repr__(self):
        return f'<Gear {self.name}>'

class Damagetype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    weap_source = db.relationship("Weapon", secondary=weap_dmg_type_table, back_populates="dmg_type")
    race_resist = db.relationship("Race", secondary=race_dmg_resist_table, back_populates="dmg_resist")
    race_immune = db.relationship("Race", secondary=race_dmg_immune_table, back_populates="dmg_immune")
    race_vulner = db.relationship("Race", secondary=race_dmg_vulner_table, back_populates="dmg_vulner")
    cls_resist = db.relationship("Cls_5e", secondary=cls_dmg_resist_table, back_populates="dmg_resist")
    cls_immune = db.relationship("Cls_5e", secondary=cls_dmg_immune_table, back_populates="dmg_immune")
    cls_vulner = db.relationship("Cls_5e", secondary=cls_dmg_vulner_table, back_populates="dmg_vulner")
    feature_resist = db.relationship("Feature", secondary=feature_dmg_resist_table, back_populates="dmg_resist")
    feature_immune = db.relationship("Feature", secondary=feature_dmg_immune_table, back_populates="dmg_immune")
    feature_vulner = db.relationship("Feature", secondary=feature_dmg_vulner_table, back_populates="dmg_vulner")
    armor_resist = db.relationship("Armor", secondary=armor_dmg_resist_table, back_populates="dmg_resist")
    armor_immune = db.relationship("Armor", secondary=armor_dmg_immune_table, back_populates="dmg_immune")
    armor_vulner = db.relationship("Armor", secondary=armor_dmg_vulner_table, back_populates="dmg_vulner")
    ammo_source = db.relationship("Ammo_power", secondary=ammo_power_dmg_type_table, back_populates="dmg_type")

    def __repr__(self):
        return f'<Damagetype {self.name}>' 

class Dice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    value = db.Column(db.Integer)
    damage_roller = db.relationship("Weapon", secondary=weap_dice_table, back_populates="damage_dice")
    cls_hit_dice = db.relationship("Cls_5e", secondary=cls_hit_dice_table, back_populates="hit_dice_type")

    def __repr__(self):
        return f'<Dice {self.name}>'

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    members = db.relationship("Character", secondary=char_party_table, back_populates="parties")
    max_members = db.Column(db.Integer)
    joined_game = db.relationship("Game", secondary=game_party_table, back_populates="adventurers")

    def __repr__(self):
        return f'<Party {self.name}>'

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    adventurers = db.relationship("Party", secondary=game_party_table, back_populates="joined_game")
    gm = db.relationship("User", secondary=user_game_table, back_populates="games")
    npcs = db.relationship("Npcpool", secondary=game_npc_pool_table, back_populates="game")

    def __repr__(self):
        return f'<Game {self.name}>'

class Npcpool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    picked_npc = db.relationship("Character", secondary=char_npc_pool_table, back_populates="npc_group")
    game = db.relationship("Game", secondary=game_npc_pool_table, back_populates="npcs")

    def __repr__(self):
        return f'<Npcpool {self.name}>'
