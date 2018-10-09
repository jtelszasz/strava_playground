from urllib.request import urlopen
import json
import sqlite3
import ssl

from app import app

def get_my_activities():
    context = ssl._create_unverified_context()
    url = "https://www.strava.com/api/v3/athlete/activities?access_token=" + app.config['STRAVA_TOKEN']

    json_obj = urlopen(url, context = context)

    json_data = json.load(json_obj)

    return json_data