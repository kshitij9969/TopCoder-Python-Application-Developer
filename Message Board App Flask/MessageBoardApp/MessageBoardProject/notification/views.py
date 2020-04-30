from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from MessageBoardProject.projects.forms import CreateProject, UpdateProject, AddAssociates
from MessageBoardProject.activity.forms import CreateActivity
from MessageBoardProject.notification.forms import NotificationForm
from MessageBoardProject.models import User, Project, ProjectStatus, Budget, Activities, Notification
from MessageBoardProject import db, mail
from flask_mail import Message

notification = Blueprint('notification', __name__)


@notification.route('/send_notification', methods=['GET', 'POST'])
@login_required
def send_notification():
    print('I am here')
    project = Project.query.get(current_user.associated_project_id)
    print(project)
    users = User.query.filter_by(associated_project_id=project.project_id)
    print(users)
    form = NotificationForm()
    print('Here1')
    sender = current_user
    receiver_list = [(user.id, user.first_name + ' ' + user.last_name) for user in users]
    if not receiver_list:
        form.receivers.choices = [(-1, 'No receiver available')]
    else:
        form.receivers.choices = receiver_list
    print(form.receivers.choices)
    if form.validate_on_submit():
        notification = Notification(
            subject=form.subject.data,
            message=form.message.data
        )
        notification.sender=sender
        receiver_id = form.receivers.data
        print(type(receiver_id))
        if not (-1 in receiver_id):
            for selected_user_id in receiver_id:
                notification.user.append(User.query.get(selected_user_id))
        db.session.add(notification)
        db.session.commit()
        print(type(form.subject.data))
        print(form.subject.data)
        print(type(form.message.data))
        print(type(form.receivers.data))
        print(current_user.email)
        print('Sender email' + sender.email)
        print(type(sender.email))
        message = Message(
            subject=form.subject.data,
            sender='kshitijsingh661@gmail.com',
            recipients=list(user.email for user in notification.user)
        )
        message.body = 'Hello, you have received a notification from ' + notification.sender.first_name + ' ' +\
                       notification.sender.last_name +' and the message is '\
                       + form.message.data + '.'
        mail.send(message)
        return redirect(url_for('core.index'))
    flash(form.errors)
    return render_template('send_notification.html', form=form)