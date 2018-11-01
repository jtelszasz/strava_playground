from urllib.request import urlopen
import requests
import json
import ssl

from app import app

def get_my_activities_json():

    context = ssl._create_unverified_context()
    per_page = 200 # max per Strava API docs
    page = 1

    query_dict = { "access_token" : app.config["STRAVA_TOKEN"],
                   "per_page" : per_page,
                   "page" : page}

    url = "https://www.strava.com/api/v3/athlete/activities"


    json_data = []

    while True:
        request = requests.get(url, params=query_dict).json()

        if len(request) == 0:
            break

        for activity in request:
            json_data.append(activity)


        query_dict["page"] += 1
    return json_data

def create_activities_table(cursor):
    #cols = list(json_data[1].keys())
    q = ('CREATE TABLE IF NOT EXISTS activities('
         'id INTEGER PRIMARY KEY, '
         'start_date_local DATETIME, '
         'distance REAL'
         ')')
    cursor.execute(q)