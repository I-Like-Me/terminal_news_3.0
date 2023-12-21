from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, SelectMultipleField, widgets, StringField, IntegerField, BooleanField
from wtforms.validators import Length, NumberRange, DataRequired
from wtforms_alchemy import QuerySelectMultipleField, QuerySelectField


# SelectFeild used to pick Class.
class PickCls(FlaskForm):
    cls = SelectField('Class', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

# SelectFeild used to pick Subject.
class PickSubject(FlaskForm):
    subject = SelectField('Subject', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(html_tag='ul', prefix_label=True)
    option_widget = widgets.CheckboxInput()

class PickTopics(FlaskForm):
    topics = MultiCheckboxField('topics', choices=[
        ('char_name', 'Name'), ('birth_name', 'Birth Name'), ('age', 'Age'),
        ('real_age', 'Real Age'), ('cur_race', 'Current Race'), ('birth_race', 'Birth Race'),
        ('cur_loc', 'Current Location'), ('birth_loc', 'Birth Location'),
        ('public_history', 'Public History'), ('learned_history', 'Learned History'),
        ('hidden_history', 'Hidden History'), ('cls', 'Class'), ('arch', 'Architype'),
        ('faction', 'Faction'), ('rank', 'Rank'), ('cybernetics', 'Cybernetics'),
        ('job', 'Job'), ('spliced', 'Spliced'), ('robot', 'Robot')])
    submit = SubmitField('Submit')

class PickNPCs(FlaskForm):
    npcs = QuerySelectMultipleField("NPCs")

class AssetAdder(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    race = QuerySelectField("Races")
    background = QuerySelectField("Backgrounds")
    alignment = QuerySelectField("Classes")

    starting_cls = QuerySelectField("Classes")
    submit = SubmitField('Submit')

class AssetSel(FlaskForm):
    asset_type = SelectField('types', choices=[
        ('Ability', 'Ability'), ('Alignment', 'Alignment'), ('Ammo_power', 'Ammo and Power'),
        ('Architype', 'Architype'), ('Armor', 'Armor'), ('Background', 'Background'),
        ('Character', 'Character'), ('Cls_5e', 'Class'), ('Cybernetic', 'Cybernetic'), 
        ('Damagetype', 'Damage Type'), ('Dice', 'Dice'), ('Faction', 'Faction'), 
        ('Feat', 'Feat'), ('Feature', 'Feature'), ('Gear', 'Gear'), ('Ladder', 'Ladder'),
        ('Location', 'Location'), ('Mech', 'Mech'), ('Property', 'Property'), 
        ('Race', 'Race'), ('Rank', 'Rank'), ('Skill', 'Skill'), ('Spell', 'Spell'), 
        ('Vehicle', 'Vehicle'), ('Weapon', 'Weapon')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class CharacterForm(FlaskForm):
    name = StringField('Name')
    birth_name = StringField('Birth Name')
    strength = IntegerField('Strength', [NumberRange(min=0, max=100)])
    dexterity = IntegerField('Dexterity', [NumberRange(min=0, max=100)])
    constitution = IntegerField('Constitution', [NumberRange(min=0, max=100)])
    intelligence = IntegerField('Intelligence', [NumberRange(min=0, max=100)])
    wisdom = IntegerField('Wisdom', [NumberRange(min=0, max=100)])
    charisma = IntegerField('Charisma', [NumberRange(min=0, max=100)])
    background = QuerySelectField("Backgrounds")
    alignment = QuerySelectField("Alignment")
    classes = QuerySelectField("Class")
    cur_race = QuerySelectField("Race")
    birth_race = QuerySelectField("Birth Race")
    age = IntegerField('Age')
    real_age = IntegerField('Real Age')
    cur_loc = IntegerField('Current Location')
    birth_loc = IntegerField('Birth Location')
    job = StringField('Job')
    job_desc = TextAreaField('Job Description')
    spliced = BooleanField('Spliced')
    robot = BooleanField('Robot')
    pure = BooleanField('Pure')
    npc = BooleanField('NPC')


class AbilityForm(FlaskForm):
    pass
