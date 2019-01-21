from app import app, db
from app.analytics import get_my_activities_json
from app.models import Activity
from flask import render_template
from datetime import datetime
import pandas as pd

db.create_all()
db.session.commit()

@app.route('/')
@app.route('/index')
def index():
    # get activities from strava
    activities_json = get_my_activities_json()

    for item in activities_json:
        if db.session.query(Activity).filter_by(id=item["id"]).scalar() is None:
            act = Activity(
                id = item["id"],
                distance = item["distance"],
                start_date = datetime.strptime(item["start_date_local"],
                                               '%Y-%m-%dT%H:%M:%SZ'),
                bike = item["gear"]["name"],
                elapsed_time = item["elapsed_time"],
                moving_time = item["moving_time"]
            )
            db.session.add(act)

    db.session.commit()

    n_acts = db.session.query(Activity).count()

    activities = pd.read_sql(db.session.query(Activity).statement, db.engine)

    return render_template('index.html', title="Justin's Strava Playground", n_acts=n_acts, activities=activities)