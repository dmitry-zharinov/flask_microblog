from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from logging.handlers import RotatingFileHandler
import logging
import os

flask_app = Flask(__name__, static_url_path='/static')
flask_app.config.from_object(Config)
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)
moment = Moment(flask_app)
login = LoginManager(flask_app)
login.login_view = 'login'
mail = Mail(flask_app)
bootstrap = Bootstrap(flask_app)

if not flask_app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    flask_app.logger.addHandler(file_handler)

    flask_app.logger.setLevel(logging.INFO)
    flask_app.logger.info('Microblog startup')

from app import routes, models, errors
