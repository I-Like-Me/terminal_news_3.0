from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, SelectMultipleField, widgets
from wtforms.validators import Length, DataRequired


# SelectFeild used to pick Class.
class PickCls(FlaskForm):
    app = SelectField('Class', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

# SelectFeild used to pick Subject.
class PickSubject(FlaskForm):
    app = SelectField('Subject', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

class PickTopics(FlaskForm):
    app = SelectField('topics', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddWeapon(FlaskForm):
    description = TextAreaField('Content', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')