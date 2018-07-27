
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
         'start_date_local DATETIME '
         'distance FLOAT'
         ')')

    #c.execute("sdf")

def activities_to_sql():
    '''insert into activities table'''
    c.execute("INSERT INTO activities values(?, ?)")
    c.commit()

def main():
    #create_activities_table()

    json_data = get_my_activities()



    for item in json_data:
        print(item["start_date_local"])
        print(item["distance"])

    return(json_data)




if __name__ == "__main__":
    json_data = main()