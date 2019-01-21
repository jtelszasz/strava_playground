from app import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.DateTime, nullable = False)
    distance = db.Column(db.Float, nullable = False)
    bike = db.Column(db.String, nullable = True)
    elapsed_time = db.Column(db.Float, nullable = False)
    moving_time = db.Column(db.Float, nullable=False)
    total_elev_gain = db.Column(db.Float, nullable=True)
    avg_speed = db.Column(db.Float, nullable=True)
    max_speed = db.Column(db.Float, nullable=True)
    trainer = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return '<Start Date {}>'.format(self.start_date)