import os


class Configuration(object):

    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') # TODO изменить и добавить в переменные среды
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db?check_same_thread=False'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
