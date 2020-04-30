from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed


class NotificationForm(FlaskForm):
    subject = StringField('Subject:', validators=[DataRequired()])
    message = StringField('Message:', validators=[DataRequired()])
    receivers = SelectMultipleField('Send to:', coerce=int, validators=[DataRequired()])
    send = SubmitField('Send')