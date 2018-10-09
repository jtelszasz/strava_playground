import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    STRAVA_TOKEN = os.environ.get('STRAVA_TOKEN')
    STRAVA_SECRET = os.environ.get('STRAVA_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'strava.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
