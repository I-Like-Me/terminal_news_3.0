from app import db
from sqlalchemy.ext.associationproxy import association_proxy

user_char_table = db.Table(
    "user_char_table",
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("character_id", db.ForeignKey("character.id"), primary_key=True),
)


class CharCls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column("character_id", db.Integer, db.ForeignKey("character.id"))
    cls_5e_id = db.Column("cls_5e_id",db.Integer , db.ForeignKey("cls_5e.id"))
    cls_level = db.Column(db.Integer)

    classed_character = db.relationship("Character", back_populates='cls_association')
    cls = db.relationship("Cls_5e", back_populates='classed_character_association')

    # def lvl_up_cls(self, cls_target):
    #     for cls
    #     self.cls_level += 1
   

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
    cls_association = db.relationship("CharCls", back_populates="classed_character")
    classes = association_proxy("cls_association", "cls")
    level = db.Column(db.Integer)
    npc = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Character {self.name}>'

    def pick_cls(self, cls_pick):
        char_cls_ready = CharCls(classed_character=self, cls=cls_pick, cls_level=1)
        db.session.add(char_cls_ready)
        db.session.commit()
        

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