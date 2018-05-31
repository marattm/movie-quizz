# services/quizz/project/config.py

import os


class BaseConfig:
    '''Base configuration'''
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='password'


class DevelopmentConfig(BaseConfig):
    '''Development configuration'''
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    '''testing configuration'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    '''Production configuration'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
