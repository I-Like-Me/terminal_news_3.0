from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Length

class Add_Content(FlaskForm):
    content = TextAreaField('Content', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')