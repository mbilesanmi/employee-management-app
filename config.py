# config.py

class Config(object):
    """
    Common configurations
    """

    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}