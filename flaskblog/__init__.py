from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import Configuration
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Configuration):
    app = Flask(__name__)
    app.config.from_object(Configuration)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app


# TODO: добавить WhiteList доступных для регистрации email'ов
# TODO: Добавить логгирование
# TODO: Добавить тестирование
# TODO: Добавить ассоциативную таблицу many-to-many для тегов
# TODO: Добавить теги к постам
# TODO: Добавить поисковый движок по тексту поста
# TODO: Добавить в сайдбар категории и сортировку по ним( через теги я так полагаю)
# TODO: Добавить дропзону в посты для картинок (FLASK-Dropzone?)
# TODO: Добавить админку (FLASK-Admin)
# TODO: Изменить стили
# TODO: Добавить календарь.
