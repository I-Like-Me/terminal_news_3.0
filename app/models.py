from app import db
from sqlalchemy.ext.associationproxy import association_proxy

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

armor_dmg_type_table = db.Table(
    "armor_dmg_type_table",
    db.Column("armor_id", db.ForeignKey("armor.id"), primary_key=True),
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

class CharCls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_cls = db.Column(db.String(64), index=True, unique=True)
    character_id = db.Column("character_id", db.Integer, db.ForeignKey("character.id"))
    cls_5e_id = db.Column("cls_5e_id",db.Integer , db.ForeignKey("cls_5e.id"))
    cls_level = db.Column(db.Integer)

    classed_character = db.relationship("Character", back_populates='cls_association')
    cls = db.relationship("Cls_5e", back_populates='classed_character_association')
   
    def __repr__(self):
        return f'<CharCls {self.char_cls}>'

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
    ladder =
    background =
    alignment =
    factions = 
    ability_numbers = db.relationship("AbilityScores", back_populates="able_char")
    pro_skills =
    skill_numbers = db.relationship("SkillScores", back_populates="skilled_char")
    cls_association = db.relationship("CharCls", back_populates="classed_character")
    classes = association_proxy("cls_association", "cls")
    life_info = db.relationship("Lifeinfo", back_populates="life_info_holder")
    cls_info = db.relationship("Clsinfo", back_populates="cls_info_holder") #convert to many to many
    weapons = 
    armor = 
    gear =
    prepd_spells =
    spellbook =
    feats =
    backpack = db.Column(db.String(5000))
    play_notes = db.Column(db.String(5000))
    npc = db.Column(db.Boolean)
    npc_group = db.relationship("Npcpool", secondary=char_npc_pool_table, back_populates="picked_npc")

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
    
    def __repr__(self):
        return f'<Cls_5e {self.name}>'

    def new_cls_adder(cls_name):
        new_cls = Cls_5e(name=cls_name)
        db.session.add(new_cls)
        db.session.commit()

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    race_features =
    char_cur_race =
    char_birth_race =

    def __repr__(self):
        return f'<Race {self.name}>'

    def new_race_adder(race_name):
        new_race = Race(name=race_name)
        db.session.add(new_race)
        db.session.commit()

class Background(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    char_bg =

    def __repr__(self):
        return f'<Background {self.name}>'

    def new_race_adder(bg_name):
        new_bg = Background(name=bg_name)
        db.session.add(new_bg)
        db.session.commit()

class Architype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    arch_features = db.relationship("Feature", secondary=arch_feature_table, back_populates="featured_arch")
    arched_cls = db.relationship("Cls_5e", secondary=cls_arch_table, back_populates="arch_choices")

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
    featured_arch =

    def __repr__(self):
        return f'<Feature {self.name}>'

class Ability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    cls_sav_throw = db.relationship("Cls_5e", secondary=cls_sav_ability_table, back_populates="sav_throws")

    def __repr__(self):
        return f'<Ability {self.name}>'

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(1000))
    char_cur_loc =  
    char_birth_loc = 

    def __repr__(self):
        return f'<Location {self.name}>'

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    skl_trained_cls = db.relationship("Cls_5e", secondary=cls_pro_skill_table, back_populates="skill_pro_choice")

    def __repr__(self):
        return f'<Skill {self.name}>'

class Lifeinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(64), index=True, unique=True)
    birth_name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    real_age  = db.Column(db.Integer)
    cur_race =
    birth_race =
    cur_loc =  
    birth_loc = 
    public_history = db.Column(db.String(5000))
    learned_history = db.Column(db.String(5000))
    hidden_history = db.Column(db.String(5000))
    life_info_holder = db.relationship("Character", back_populates="life_info")

    def __repr__(self):
        return f'<Lifeinfo {self.char_name}>'

class Clsinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(64), index=True, unique=True)
    arch = 
    total_hit_dice = db.Column(db.String(64))
    cur_hit_dice = db.Column(db.String(64))
    cls_info_holder = db.relationship("Character", back_populates="cls_info") #convert to many to many

    def __repr__(self):
        return f'<Clsinfo {self.name}>'

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
    skilled_char = db.relationship("Character", back_populates="skill_numbers")

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
    able_char = db.relationship("Character", back_populates="ability_numbers")

    def __repr__(self):
        return f'<AbilityScores {self.char_name}>'

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    damage_dice = db.relationship("Dice", secondary=weap_dice_table, back_populates="damage_roller")
    num_of_dice = db.Column(db.Integer)
    dmg_type = db.relationship("DamageType", secondary=weap_dmg_type_table, back_populates="weap_source")
    properties = db.relationship("Property", secondary=weapon_property_table, back_populates="weap_prop")
    tech_level = db.Column(db.Integer)
    ranged = db.Column(db.Boolean)
    reach = db.Column(db.Integer)
    normal_range = db.Column(db.Integer)
    long_range = db.Column(db.Integer)
    martial = db.Column(db.Boolean)
    weap_trained_cls = db.relationship("Cls_5e", secondary=cls_pro_weap_table, back_populates="weap_pros")
    wielder = 

    def __repr__(self):
        return f'<Weapon {self.name}>'

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200))
    weap_prop = db.relationship("Weapon", secondary=weapon_property_table, back_populates="properties")

    def __repr__(self):
        return f'<Property {self.name}>'

class Armor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    armor_size = db.Column(db.String(64))
    ac = db.Column(db.Integer)
    ac_mod_type =
    ac_mod_max = db.Column(db.Integer)
    str_req = db.Column(db.Integer)
    stealth = db.Column(db.String(64))
    resist_type = db.relationship("DamageType", secondary=armor_dmg_type_table, back_populates="armor_source")
    armor_trained_cls = db.relationship("Cls_5e", secondary=cls_pro_armor_table, back_populates="armor_pros") 
    wearer = 

    def __repr__(self):
        return f'<Armor {self.name}>'

class Gear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    tool_trained_cls = db.relationship("Cls_5e", secondary=cls_pro_tool_table, back_populates="tool_pros")
    owner = 

    def __repr__(self):
        return f'<Gear {self.name}>'

class Damagetype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    weap_source = db.relationship("Weapon", secondary=weap_dmg_type_table, back_populates="dmg_type")
    armor_source = db.relationship("Armor", secondary=armor_dmg_type_table, back_populates="dmg_type")
    race_source =
    cls_source =

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