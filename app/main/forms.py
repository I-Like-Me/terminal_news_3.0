from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, SelectMultipleField, widgets, StringField, IntegerField, BooleanField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, ValidationError
from wtforms_alchemy import QuerySelectMultipleField, QuerySelectField
from app import db
from app.models import Character, Ability, Background, Alignment, Cls_5e, Race, Location, Ladder, Skill, Feat, Rank, Faction, Damagetype, Feature


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

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
    skill_pro_choice = QuerySelectField("Select Skills")
    ladder = QuerySelectField("Ladder")
    cur_race = QuerySelectField("Race")
    birth_race = QuerySelectField("Birth Race")
    age = IntegerField('Age', [NumberRange(min=0, max=10000)])
    real_age = IntegerField('Real Age', [NumberRange(min=0, max=10000)])
    cur_loc = QuerySelectField('Current Location')
    birth_loc = QuerySelectField('Birth Location')
    job = StringField('Job')
    job_desc = TextAreaField('Job Description')
    spliced = BooleanField('Spliced')
    robot = BooleanField('Robot')
    pure = BooleanField('Pure')
    npc = BooleanField('NPC')
    char_sum = TextAreaField('Character Summery')
    submit = SubmitField('Submit')

class AbilityForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        ability = Ability.query.filter_by(name=name.data.lower()).first()
        if ability is not None:
            raise ValidationError('Please use a different name.')
        if name.data[0] == ' ':
            raise ValidationError('Please remove leading white space.')
        if name.data[-1] == ' ':
            raise ValidationError('Please remove trailing white space.')
        

class SkillForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    ability = QuerySelectField("Ability", validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        skill = Skill.query.filter_by(name=name.data.lower()).first()
        if skill is not None:
            raise ValidationError('Please use a different name.')
        if name.data[0] == ' ':
            raise ValidationError('Please remove leading white space.')
        if name.data[-1] == ' ':
            raise ValidationError('Please remove trailing white space.')
        
    # def validate_ability(self, ability):                                            

    #     if len(ability.data) != 1:                                          
    #         raise ValidationError('Please only select 1 item')    
   

class Location(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

    def validate_name(self, name):
        location = Location.query.filter_by(name=name.data.lower()).first()
        if location is not None:
            raise ValidationError('Please use a different name.')
        if name.data[0] == ' ':
            raise ValidationError('Please remove leading white space.')
        if name.data[-1] == ' ':
            raise ValidationError('Please remove trailing white space.')

# Missing fields
class BackgroundForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    extra_languages_num = IntegerField('Number of extra languages', [NumberRange(min=0, max=10)])
    submit = SubmitField('Submit')

class AlignmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class FactionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    fac_ranks = QuerySelectMultipleField("Select Ranks")
    submit = SubmitField('Submit')

class RankForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class ArchitypeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class FeatForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class FeatureForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    level_access = IntegerField('Level Access', [NumberRange(min=0, max=100)])
    dmg_resist = QuerySelectMultipleField("Select Damage Resistance")
    dmg_immune = QuerySelectMultipleField("Select Damage Immunity")
    dmg_vulner = QuerySelectMultipleField("Select Damage Vulnerability")
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class PropertyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class DamagetypeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        damagetype = Damagetype.query.filter_by(name=name.data.lower()).first()
        if damagetype is not None:
            raise ValidationError('Please use a different name.')
        if name.data[0] == ' ':
            raise ValidationError('Please remove leading white space.')
        if name.data[-1] == ' ':
            raise ValidationError('Please remove trailing white space.')    

class DiceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    value = IntegerField('Dice Value', [NumberRange(min=0, max=100)])
    submit = SubmitField('Submit')