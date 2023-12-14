from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, SelectMultipleField, widgets
from wtforms.validators import Length, DataRequired
from wtforms_alchemy import QuerySelectMultipleField


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

class AddWeapon(FlaskForm):
    description = TextAreaField('Content', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')