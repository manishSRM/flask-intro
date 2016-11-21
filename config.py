class BaseConfig(object):

    DEBUG = False
    SECRET_KEY = "my key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False