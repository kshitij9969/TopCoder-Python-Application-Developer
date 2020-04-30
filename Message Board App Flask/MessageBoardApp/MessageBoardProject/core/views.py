from flask import Blueprint, render_template
from flask_login import login_required, login_user, current_user, logout_user
from MessageBoardProject.models import Project, User, ProjectStatus, Activities, Notification

core = Blueprint('core', __name__)


@core.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        user = current_user
        if user.associated_project_id:
            project_details = Project.query.get(user.associated_project_id)
            project_status = ProjectStatus.query.get(project_details.project_status_id)
            status_dict = dict((col, getattr(project_status, col)) for col in project_status.__table__.columns.keys())
            present_progress = 0
            for status, status_condition in status_dict.items():
                print(status_condition)
                if status_condition == True and type(status_condition) == bool:
                    present_progress += 1
            present_progress = (present_progress * 100 )/4
            activities = current_user.activity
            notifications = Notification.query.filter_by(sender_id=current_user.id)
            notifications_recieved = Notification.query.join(User.notification).filter(User.id == current_user.id).all()
    if current_user.designation=='Project Manager':
        associates_reporting = User.query.filter_by(reports_to_user=current_user)
    return render_template('index.html', **locals())


@core.route('/permissions')
def permissions():
    return render_template('permissions.html')