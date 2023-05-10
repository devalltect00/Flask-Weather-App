class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'mysecretkey'
    API_KEY = '927277edbe8f004719fab24f02a108fd'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
