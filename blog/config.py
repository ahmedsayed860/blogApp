import os


class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = "jaVfcQMEu33YktoqoQ-_zw"


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass
