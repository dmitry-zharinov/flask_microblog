from app import flask_app
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm

@flask_app.route('/')
@flask_app.route('/index')
def index():
    title = 'Welcome'
    user = {'username': 'Dmitry'}
    posts = [{
        'author': user,
        'body': "Lorem ipsum"}]

    return render_template('index.html', user = user, title = title, posts = posts)


@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.rememberMe.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)