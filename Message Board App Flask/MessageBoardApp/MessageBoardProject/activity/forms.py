from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed


class CreateActivity(FlaskForm):
    activity_title=StringField('Activity title:', validators=[DataRequired()])
    activity_details=StringField('Activity details:', validators=[DataRequired()])
    activity_date = DateField('Activity date:', validators=[DataRequired()], format='%Y-%m-%d')
    activity_user = SelectMultipleField('Add users', coerce=int)
    add_activity = SubmitField('Add Activity')


