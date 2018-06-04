# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Dmitry'}
    posts = [
        {
            'author': {'username': 'm1rko'},
            'body': 'Как безопасно программировать в bash'
        },
        {
            'author': {'username': 'mkulesh'},
            'body': 'Отладочная плата STM32F4 в форм-факторе Raspberry Pi'
        }, 
        {
            'author': {'username': 'mi5ha6in'},
            'body': 'CSRF-уязвимости все еще актуальны'
        }]
    return render_template('index.html', title = 'Home', user = user, posts = posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Вход', form=form)

