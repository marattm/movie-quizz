# services/quizz/project/config.py


class BaseConfig:
    '''Base configuration'''
    TESTING = False


class DevelopmentConfig(BaseConfig):
    '''Development configuration'''
    TESTING = False


class TestingConfig(BaseConfig):
    '''testing configuration'''
    TESTING = True


class ProductionConfig(BaseConfig):
    '''Production configuration'''
    pass
