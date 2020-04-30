from MessageBoardProject.models import User
from wtforms import StringField, PasswordField,SelectField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    username = StringField('username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    login = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    designation = SelectField('Designation:',
                              choices=[('Project Manager', 'Project Manager'),('Associate', 'Associate')],
                              validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired()])
    register = SubmitField('Register')

    def check_unique_username(self, username):
        if User.query.filter_by(username=username):
            raise ValidationError('A user already exist with that username, please choose another one.')

    def check_unique_email(self, email):
        if User.query.filter_by(email=email):
            raise ValidationError('A user already exist with that email, please choose another one.')


class UpdateUserForm(FlaskForm):
    first_name = StringField('First name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    update = SubmitField('Update')

    def check_unique_username(self, username):
        if User.query.filter_by(username=username):
            raise ValidationError('A user already exist with that username, please choose another one.')

    def check_unique_email(self, email):
        if User.query.filter_by(email=email):
            raise ValidationError('A user already exist with that email, please choose another one.')


