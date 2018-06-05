# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dmitry'}
    posts = [{'author': {'username': 'csrfb'},
             'body': 'CSRF-уязвимости все еще актуальны'},
             {'author': {'username': 'ghub'},
             'body': 'GitHub теперь официально принадлежит Microsoft'},
             {'author': {'username': 'GlobalSign_admin'},
             'body': 'АНБ предложило стандарт шифрования для устройств Интернета вещей, но ISO его отвергло'},
             {'author': {'username': 'SMDP'},
             'body': 'Стрелочные LED-часы для обучения пайке SMD компонентов'},
             {'author': {'username': 'trienergy'},
             'body': 'Токамак JET начинает новую дейтерий-тритиевую кампанию'}]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Пользователь {} успешно авторизован с опцией "запомнить меня" {}'.format(
                form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Вход', form=form)
