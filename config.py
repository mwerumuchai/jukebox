import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_AUDIOS_DEST = 'app/static/audios'

class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://muchai:muchai90@localhost/nick_box_test'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://carol:carol1@localhost/nick_box_test'



class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://muchai:muchai90@localhost/nick_box'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://carol:carol1@localhost/nick_box'


    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
