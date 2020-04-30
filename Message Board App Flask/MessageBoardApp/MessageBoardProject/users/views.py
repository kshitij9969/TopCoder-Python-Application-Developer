from flask import render_template, url_for, flash, redirect, Blueprint, request, abort
from flask_login import login_required, login_user, current_user, logout_user
from MessageBoardProject import db, app
from MessageBoardProject.users.forms import RegistrationForm, UpdateUserForm, LoginForm
from MessageBoardProject.models import User
users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                password=form.password.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                designation=form.designation.data,
            )
            db.session.add(user)
            db.session.commit()
            flash('Registered successfully, please continue to login!')
            return redirect(url_for('users.user_login'))
    return render_template('users/registration.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    # if request.method == 'POST':
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash(f'Welcome, {user.first_name} {user.last_name}!')
            next = request.args.get('next')

            if next is None or next[0] == '/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('users/login.html', form=form)


@users_blueprint.route('/update', methods=['GET', 'POST'])
@login_required
def update_user():
    form = UpdateUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = current_user
            if current_user.is_authenticated:
                user = User.query.filter_by(username=current_user.username).first()
            else:
                abort(403)
            if user.check_password(form.password.data):
                user_update = User(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                )
                db.session.add(update_user)
                db.session.commit()
                flash('Details updated!')
                return redirect(url_for('core.index'))

    return render_template('users/update_user.html', form=form)


@users_blueprint.route('/view_details', methods=['GET','POST'])
@login_required
def view_details():
    if current_user.is_authenticated:
        email = current_user.email
        first_name = current_user.first_name
        last_name = current_user.last_name
        username = current_user.username
        designation = current_user.designation
        return render_template('users/view_details.html', email=email,
                               first_name=first_name,
                               last_name=last_name,
                               username=username,
                               designation=designation)
    else:
        abort(403)


@users_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))