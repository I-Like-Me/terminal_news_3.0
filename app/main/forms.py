from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, SelectMultipleField, widgets, StringField, RadioField
from wtforms.validators import Length, DataRequired
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
    chars = QuerySelectField("Chars")
