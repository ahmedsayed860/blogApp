import os


class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = "jaVfcQMEu33YktoqoQ-_zw"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass
