from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from MessageBoardProject.projects.forms import CreateProject, UpdateProject, AddAssociates
from MessageBoardProject.activity.forms import CreateActivity
from MessageBoardProject.models import User, Project, ProjectStatus, Budget, Activities
from MessageBoardProject import db


activity = Blueprint('activity', __name__)


@activity.route('/add_activity', methods=['GET', 'POST'])
@login_required
def add_activity():
    users = User.query.all()
    print(users)
    form = CreateActivity()
    print('Here1')
    users_list = [(user.id, user.first_name + ' ' + user.last_name) for user in users]
    if not users_list:
        form.activity_user.choices = [(-1, 'No associates available')]
    else:
        form.activity_user.choices = users_list
    print(form.activity_user.choices)
    if form.validate_on_submit():
        activity = Activities(
            activity_title=form.activity_title.data,
            activity_details=form.activity_details.data,
            activity_date=form.activity_date.data
        )
        users_list_id = form.activity_user.data
        if not (-1 in users_list_id):
            for selected_user_id in users_list_id:
                activity.user.append(User.query.get(selected_user_id))
                activity.user.append(current_user)
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for('core.index'))
    flash(form.errors)
    return render_template('create_activity.html', form=form)