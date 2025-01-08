from app import db


class Employee(db.Model):
    __tablename__ = 'employees'  

    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    date_of_joining = db.Column(db.Date, nullable=False)
