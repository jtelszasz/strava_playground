
import config
from urllib.request import urlopen
import json
import sqlite3

conn = sqlite3.connect("strava.db")
c = conn.cursor()

def get_my_activities():
    url = "https://www.strava.com/api/v3/athlete/activities?access_token=" + config.ACCESS_TOKEN

    json_obj = urlopen(url)

    json_data = json.load(json_obj)

    return json_data

def create_activities_table(json_data):
    cols = list(json_data[1].keys())
    q = ('CREATE TABLE IF NOT EXISTS activities('
         'start_date_local DATETIME, '
         'distance REAL'
         ')')

    c.execute(q)

def activities_to_sql(json_data):
    '''insert into activities table'''

    for item in json_data:

        print(item["start_date_local"])
        print(item["distance"])

        c.execute("INSERT INTO activities(start_date_local, distance) VALUES(?, ?)",
                  (item["start_date_local"],
                   item["distance"]))

def main():
    #create_activities_table()

    json_data = get_my_activities()

    create_activities_table(json_data)

    activities_to_sql(json_data)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()