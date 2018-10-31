from urllib.request import urlopen
import requests
import json
import ssl

from app import app

def get_my_activities_json():

    context = ssl._create_unverified_context()
    per_page = 100
    page = 1

    query_dict = { "access_token" : app.config["STRAVA_TOKEN"],
                   "per_page" : per_page,
                   "page" : page}
    url = "https://www.strava.com/api/v3/athlete/activities"

    response = requests.get(url, params=query_dict).json()
    json_data = response
    # old way
    #json_obj = urlopen(url, context = context)
    #json_data = json.load(json_obj)

    return json_data

def create_activities_table(cursor):
    #cols = list(json_data[1].keys())
    q = ('CREATE TABLE IF NOT EXISTS activities('
         'id INTEGER PRIMARY KEY, '
         'start_date_local DATETIME, '
         'distance REAL'
         ')')
    cursor.execute(q)