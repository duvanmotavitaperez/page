from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class Fields(FlaskForm):
    user = StringField('user', validators=[DataRequired(message='Por favor completa éste campo')])
    password = PasswordField()