from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:passwird@postgres.c5wq22yyqd4d.eu-north-1.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Timetable model
class Timetable(db.Model):
    __tablename__ = 'timetable'
    id = db.Column(db.Integer, primary_key=True)
    course_section = db.Column(db.String(20))
    credit_hours = db.Column(db.Numeric(3, 1))
    title = db.Column(db.String(255))
    instructor = db.Column(db.String(100))
    campus = db.Column(db.String(255))
    building = db.Column(db.String(255))
    room = db.Column(db.String(50))
    days = db.Column(db.String(20))
    time = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    type = db.Column(db.String(50))

@app.route('/')
def home():
    # Query all timetable entries
    timetable = Timetable.query.all()
    return render_template('timetable.html', timetable=timetable)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
