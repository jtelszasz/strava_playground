from app import app
from app.analytics import get_my_activities_json, create_activities_table
from flask import render_template
import sqlite3

@app.route('/')
@app.route('/index')
def index():
    # get activities from strava
    activities_json = get_my_activities_json()

    conn = sqlite3.connect(app.config["DATABASE_URL"])
    c = conn.cursor()

    create_activities_table(c)

    # add any new ones to the db
    for item in activities_json:

        c.execute("SELECT id FROM activities WHERE id = ?;", (int(item["id"]),))

        if not c.fetchone():
            c.execute("INSERT INTO activities(id, start_date_local, distance) VALUES(?, ?, ?)",
                      (item["id"],
                       item["start_date_local"],
                       item["distance"]))

    c.execute("SELECT COUNT(*) FROM activities;")
    n_acts = c.fetchone()[0]

    c.close()
    conn.close()


    user = {"username" : "Justin"}
    return render_template('index.html', title="Justin's Strava Playground", user=user, n_acts=n_acts, data=activities_json)