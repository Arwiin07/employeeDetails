from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Employee


class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    position = StringField('Position', validators=[DataRequired()])
    salary = FloatField('Salary', validators=[DataRequired()])
    date_of_joining = DateField('Date of Joining', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        employee = Employee.query.filter_by(email=email.data).first()
        if employee:
            raise ValidationError('Email is already in use.')
