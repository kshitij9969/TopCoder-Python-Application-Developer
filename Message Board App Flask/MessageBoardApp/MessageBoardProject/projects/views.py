from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from MessageBoardProject.projects.forms import CreateProject, UpdateProject, AddAssociates
from MessageBoardProject.models import User, Project, ProjectStatus, Budget
from MessageBoardProject import db


projects = Blueprint('projects', __name__)


@projects.route('/create_project', methods=['GET', 'POST'])
@login_required
def create_project():
    associates = User.query.filter_by(available=True).filter_by(designation='Associate').all()
    print(associates)
    form = CreateProject()
    print('Here1')
    associates_list = [(associate.id, associate.first_name + ' ' + associate.last_name) for associate in associates]
    if not associates_list:
        form.associates.choices = [(-1,'No associates available')]
    else:
        form.associates.choices = associates_list
    print(form.associates.choices)
    if form.validate_on_submit():
        budget = Budget(
            project_budget=form.budget.data
        )
        db.session.add(budget)
        project = Project(
            project_title=form.project_title.data,
            project_description=form.project_description.data,
            project_expected_end_date = form.project_end_date.data,
        )
        associates_selected_id = form.associates.data
        if not (-1 in associates_selected_id):
            for selected_associate_id in associates_selected_id:
                project.user.append(User.query.get(selected_associate_id))
                User.query.get(selected_associate_id).available=False
                db.session.add(User.query.get(selected_associate_id))
        project.user.append(current_user)
        projectstatus = ProjectStatus()
        project.project_status=projectstatus
        project.project_finance=budget
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('core.index'))
    flash(form.errors)
    return render_template('create_project.html', form=form)


@projects.route('/update_project', methods=['GET', 'POST'])
@login_required
def update_project():
    if current_user.designation=='Project Manager':
        project = Project.query.get(current_user.associated_project_id)
        form = UpdateProject()
        if form.validate_on_submit():
            project.project_title=form.project_title.data
            project.project_description=form.project_description.data
            project.project_finance.current_cost=form.budget.data
            db.session.add(project)
            db.session.commit()
            print('Hello')
            return redirect(url_for('core.index'))
        print(form.errors)
        form = UpdateProject()
        form.project_title.data = project.project_title
        form.project_description.data = project.project_description
        form.budget.data = project.project_finance.project_budget
        return render_template('update_project.html', form=form)
    return abort(403)


@projects.route('/add_associate_to_project', methods=['GET', 'POST'])
@login_required
def add_associates_to_project():
    if current_user.designation=='Project Manager':
        project = Project.query.get(current_user.associated_project_id)
        form = AddAssociates()
        associates = User.query.filter_by(available=True).filter_by(designation='Associate').all()
        form = AddAssociates()
        associates_list = [(associate.id, associate.first_name + ' ' + associate.last_name) for associate in associates]
        if not associates_list:
            form.associates.choices = [(-1, 'No associates available')]
        else:
            form.associates.choices = associates_list
        if form.validate_on_submit():
            associates_selected_id = form.associates.data
            if not (-1 in associates_selected_id):
                for selected_associate_id in associates_selected_id:
                    project.user.append(User.query.get(selected_associate_id))
                    User.query.get(selected_associate_id).available = False
                    db.session.add(User.query.get(selected_associate_id))
            db.session.add(project)
            db.session.commit()
            return redirect(url_for('core.index'))
        return render_template('add_associate_to_project.html', form=form)
    return abort(403)


@projects.route('/update_planning', methods=['GET', 'POST'])
@login_required
def update_planning():
    if current_user.designation=='Project Manager':
        project = Project.query.get(current_user.associated_project_id)
        project_status = project.project_status
        project_status.project_planning = True
        db.session.add(project_status)
        db.session.commit()
        return redirect(url_for('core.index'))
    return abort(403)


@projects.route('/update_design', methods=['GET', 'POST'])
@login_required
def update_design():
    if current_user.designation=='Project Manager':
        project = Project.query.get(current_user.associated_project_id)
        project_status = project.project_status
        if project_status.project_planning:
            project_status.project_design = True
            db.session.add(project_status)
            db.session.commit()
            return redirect(url_for('core.index'))
    return abort(403)


@projects.route('/update_development', methods=['GET', 'POST'])
@login_required
def update_development():
    if current_user.designation=='Project Manager':
        project = Project.query.get(current_user.associated_project_id)
        project_status = project.project_status
        if project_status.project_planning and project_status.project_design:
            project_status.project_development = True
            db.session.add(project_status)
            db.session.commit()
            return redirect(url_for('core.index'))
    return abort(403)


@projects.route('/update_testing', methods=['GET', 'POST'])
@login_required
def update_testing():
    if current_user.designation=='Project Manager':
        project = Project.query.get(current_user.associated_project_id)
        project_status = project.project_status
        if project_status.project_design and project_status.project_planning and project_status.project_development:
            project_status.project_testing = True
            db.session.add(project_status)
            db.session.commit()
            project = Project.query.get(current_user.associated_project_id)
            users = project.user
            for user in users:
                project.user.remove(user)
            db.session.add(project)
            db.session.commit()
            return redirect(url_for('core.index'))
    return abort(403)