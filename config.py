import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # these are configuration settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-key-is-this'