from app import db
from sqlalchemy.ext.associationproxy import association_proxy

user_char_table = db.Table(
    "user_char_table",
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
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
    proficiency = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    passive_perc = db.Column(db.Integer)
    armor_class = db.Column(db.Integer)
    inspiration = db.Column(db.Boolean)
    initiative = db.Column(db.Integer)
    cur_hit_points = db.Column(db.Integer)
    temp_hit_points = db.Column(db.Integer)
    skill_numbers = db.relationship("SkillScores", back_populates="skilled_char")
    ability_numbers = db.relationship("AbilityScores", back_populates="able_char")
    backpack = db.Column(db.String(5000))
    play_notes = db.Column(db.String(5000))
    cls_association = db.relationship("CharCls", back_populates="classed_character")
    classes = association_proxy("cls_association", "cls")
    life_info = db.relationship("Info", back_populates="info_holder")
    level = db.Column(db.Integer, default=0)
    npc = db.Column(db.Boolean)

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
    
    def __repr__(self):
        return f'<Cls_5e {self.name}>'

    def new_cls_adder(cls_name):
        new_cls = Cls_5e(name=cls_name)
        db.session.add(new_cls)
        db.session.commit()

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(64), index=True, unique=True)
    birth_name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    real_age  = db.Column(db.Integer)
    history = db.Column(db.String(5000))
    hid_history = db.Column(db.String(5000))
    info_holder = db.relationship("Character", back_populates="life_info")

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