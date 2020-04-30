# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from datetime import date, datetime


class CreateProject(FlaskForm):
    project_title = StringField('Title:', validators=[DataRequired()])
    project_description = StringField('Description:', validators=[DataRequired()])
    project_start_date = DateField('Start Date', validators=[DataRequired()], format='%Y-%m-%d')
    project_end_date = DateField('Estimated End Date', validators=[DataRequired()], format='%Y-%m-%d')
    associates = SelectMultipleField('On board associates', coerce=int)
    budget = FloatField('Budget:', validators=[DataRequired()])
    create_project = SubmitField('Create Project')

    # def validate_project_start_date(form, field):
    #     if datetime.date(datetime.strptime(str(field.data), '%Y-%m-%d')) < date.today():
    #         raise ValidationError("Project start date cannot be earlier than today!")

    def validate_project_end_date(form, field):
        if field.data < form.project_start_date.data:
            raise ValidationError('Project end date cannot be earlier than start date or today!')


class UpdateProject(FlaskForm):
    project_title = StringField('Title:', validators=[DataRequired()])
    project_description = StringField('Description:', validators=[DataRequired()])
    budget = FloatField('Budget:', validators=[DataRequired()])
    update_project = SubmitField('Update Project')


class AddAssociates(FlaskForm):
    associates = SelectMultipleField('On board associates', coerce=int)
    add = SubmitField('Add to project')