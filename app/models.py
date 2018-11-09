from app import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.DateTime, nullable = False)
    distance = db.Column(db.Float, nullable = False)

    def __repr__(self):
        return '<Start Date {}>'.format(self.start_date)