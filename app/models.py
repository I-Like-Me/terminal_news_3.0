from app import db

user_char_table = db.Table(
    "user_char_table",
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
)

char_cls_table = db.Table(
    "char_cls_table",
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
    db.Column("cls_id", db.ForeignKey("cls.id"), primary_key=True),
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    character = db.relationship("Character", secondary=user_char_table, back_populates="player")

    def __repr__(self):
        return f'<User {self.username}>'
    
    def claim_char(self, char_pick):
        if char_pick.npc != True and len(char_pick.player) == 0:
            self.character.append(char_pick)
        

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    player = db.relationship("User", secondary=user_char_table, back_populates="character")
    cls = db.relationship("Cls_5e", secondary=char_cls_table, back_populates="classed_char")
    level = db.Column(db.Integer)
    npc = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Character {self.name}>'
    
class Cls_5e(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    total_hit_dice = db.Column(db.String(64))
    cur_hit_dice = db.Column(db.String(64))
    hit_pnt_l01 = db.Column(db.Integer)
    max_num_pro_skills = db.Column(db.Integer)
    classed_char = db.relationship("Character", secondary=char_cls_table, back_populates="cls")

    def __repr__(self):
        return f'<Character {self.name}>'
