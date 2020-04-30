from MessageBoardProject import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Project(db.Model):
    __tablename__='projects'
    project_id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column(db.String(30), nullable=False, unique=True, index=True)
    project_description = db.Column(db.String(100), nullable=False, unique=True, index=True)
    project_start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    project_end_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    project_expected_end_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user = db.relationship('User', backref='project')
    project_status = db.relationship('ProjectStatus', backref=db.backref('project', uselist=False))
    project_status_id = db.Column(db.Integer, db.ForeignKey('projectstatus.id'))
    project_finance = db.relationship('Budget', backref=db.backref('project', uselist=False))
    project_finance_id = db.Column(db.Integer, db.ForeignKey('budget.id'))

    def __init__(self, project_title, project_description, project_expected_end_date):
        self.project_title=project_title
        self.project_description=project_description
        self.project_expected_end_date=project_expected_end_date

    def __str__(self):
        return f"The project name is {self.project_title}."


activity = db.Table(
    'Activity_association',
    db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('activities_id', db.Integer, db.ForeignKey('activities.id'))
)

notification = db.Table(
    'Notification_association',
    db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('notification_id', db.Integer, db.ForeignKey('notification.id'))
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    password = db.Column(db.String(128), nullable=False, unique=True, index=True)
    first_name = db.Column(db.String(128), nullable=False, unique=False, index=True)
    last_name = db.Column(db.String(128), nullable=False, unique=False, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    designation= db.Column(db.String(30), nullable=False)
    reports_to_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    reports_to_user = db.relationship('User', remote_side=[id])
    available = db.Column(db.Boolean, nullable=False, default=True)
    associated_project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    activity = db.relationship('Activities', secondary=activity, backref=db.backref('user', lazy=True))
    notification = db.relationship('Notification', secondary=notification, backref=db.backref('user', lazy=True))

    def __init__(self, username, password, email, designation, first_name, last_name):
        self.username=username
        self.password=generate_password_hash(password=password)
        self.email=email
        self.designation=designation
        self.first_name=first_name
        self.last_name=last_name

    def __str__(self):
        return f"The first name is {self.first_name} and last name is {self.last_name}."
        # if self.reports_to_user and self.associated_project:
        #     return f"Name is {self.first_name} {self.last_name}" \
        #            f" and reports to {self.reports_to_user}" \
        #            f" and works on {self.associated_project} project."
        # if self.reports_to_user:
        #     return f"Name is {self.first_name} {self.last_name}" \
        #            f"and reports to {self.reports_to_user}"
        # if self.associated_project:
        #     return f"Name is {self.first_name} {self.last_name}" \
        #            f"and works on {self.associated_project} project."

    def check_password(self, password):
        return check_password_hash(self.password, password=password)


class ProjectStatus(db.Model):
    __tablename__='projectstatus'
    id=db.Column(db.Integer, primary_key=True)
    project_planning = db.Column(db.Boolean, nullable=False, default=False)
    project_design=db.Column(db.Boolean, nullable=False, default=False)
    project_development=db.Column(db.Boolean, nullable=False, default=False)
    project_testing=db.Column(db.Boolean, nullable=False, default=False)

#
#     def __str__(self):
#         if self.project:
#             return f"This project status is associated with project {self.project}."
#         else:
#             return "This project status is not yet associated with any project."
#


class Activities(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    activity_title = db.Column(db.String(50), nullable=False, unique=True, index=True)
    activity_details = db.Column(db.String(100), nullable=False, unique=True, index=True)
    activity_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, activity_title, activity_details, activity_date):
        self.activity_title=activity_title
        self.activity_details=activity_details
        self.activity_date=activity_date

    def __str__(self):
        return f"The activity title is {self.activity_title}"


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(20), nullable=False, default='Default Subject')
    message = db.Column(db.String(50), nullable=False, default='Default Message')
    sender = db.relationship('User', backref=db.backref('sender', uselist=False))
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, subject, message):
        self.subject=subject
        self.message=message

    def __str__(self):
        return f"The notification subject is {self.subject} and the message is {self.message}"


def default_current_cost(context):
    return context.get_current_parameters()['project_budget']


class Budget(db.Model):
    __tablename__ = 'budget'
    id = db.Column(db.Integer, primary_key=True)
    project_budget = db.Column(db.Float, nullable=False, default=0)
    current_cost = db.Column(db.Float, nullable=False, default=default_current_cost)



