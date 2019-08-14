from app import flask_app
from flask import request, render_template, redirect, flash, url_for
from app.forms import LoginForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@flask_app.route('/')
@flask_app.route('/index')
@login_required
def index():
    title = 'Home Page'
    posts = [{
        'author': current_user,
        'body': "Lorem ipsum"}]

    return render_template('index.html', title = title, posts = posts)


@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() #получить объект пользователя из базы
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@flask_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))