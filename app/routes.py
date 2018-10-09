from app import app
from app.strava import get_my_activities
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    activities = get_my_activities()
    user = {"username" : "Justin"}
    return render_template('index.html', title="Justin's Strava Playground", user=user, data=activities)