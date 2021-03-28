import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False

class Prod(Config):
    DEBUG = False

class Dev(Config):
    DEVELOPMENT = True
    DEBUG = True