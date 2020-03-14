from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import Configuration
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from flaskblog import routes

# TODO: добавить WhiteList доступных для регистрации email'ов
# TODO: Добавить теги к постам
# TODO: Добавить поисковый движок
# TODO: Добавить в сайдбар категории и сортировку по ним( через теги я так полагаю)
# TODO: Добавить дропзону в посты для картинок (FLASK-Dropzone?)
# TODO: Добавить админку (FLASK-Admin)
# TODO: Изменить стили
# TODO: Добавить календарь
