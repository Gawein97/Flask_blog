import os


class Configuration(object):

    DEBUG = True
    SECRET_KEY = '83d4cea47a82c20dba816a83cbbf5366'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db?check_same_thread=False'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
