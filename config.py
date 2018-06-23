class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''

class DevConfig(Config):
    DEBUG = True
    ENVIRONMENT = 'development'