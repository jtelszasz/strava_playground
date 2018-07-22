
import config
import urllib2
import json
import sqlite3

def get_my_activities():
    url = "https://www.strava.com/api/v3/athlete/activities?access_token=" + config.ACCESS_TOKEN

    json_obj = urllib2.urlopen(url)

    json_data = json.load(json_obj)

    return json_data

def send_to_sql():
    '''send data to sqllite database'''


def main():
    json_data = get_my_activities()
    for item in json_data:
        print item["start_date_local"]
        print item["distance"]


if __name__ == "__main__":
    main()