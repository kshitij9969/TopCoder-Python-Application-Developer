import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap

# Creating an app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


# Setting up database

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MIGRATIONS'] = False

# Pass the app to SQLAlchemy class and create db object
db = SQLAlchemy(app)
Migrate(app, db)


# Set up mail notifications

app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'kshitijsingh661@gmail.com',
    MAIL_PASSWORD = 'Mumbai@123',
)


mail = Mail(app)

bootstrap = Bootstrap(app)

login_manager = LoginManager()

# On which app do you want to use login manager? --> pass the app to the login manager.
login_manager.init_app(app)

# Specify which will be the login view
login_manager.login_view = 'users.user_login'


# Configure the blueprints

from MessageBoardProject.users.views import users_blueprint
from MessageBoardProject.core.views import core
from MessageBoardProject.projects.views import projects
from MessageBoardProject.activity.views import activity
from MessageBoardProject.notification.views import notification
# Register the apps

app.register_blueprint(users_blueprint, url_prefix='/users')
# app.register_blueprint(temp)
app.register_blueprint(core)
app.register_blueprint(projects)
app.register_blueprint(activity)
app.register_blueprint(notification)

print(app.url_map)