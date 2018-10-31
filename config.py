import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    STRAVA_TOKEN = os.environ.get('STRAVA_TOKEN')
    STRAVA_SECRET = os.environ.get('STRAVA_SECRET')
    DATABASE_URL = os.environ.get('STRAVA_DB_URL') or \
                              os.path.join(basedir, 'strava.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
