from flask import render_template, redirect, url_for, flash, request, jsonify
from app import app, db
from app.models import Employee
from app.forms import EmployeeForm


@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        employee = Employee(
            name=form.name.data,
            email=form.email.data,
            position=form.position.data,
            salary=form.salary.data,
            date_of_joining=form.date_of_joining.data
        )
        db.session.add(employee)
        db.session.commit()
        flash('Employee added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_employee.html', form=form)


@app.route('/update/<int:employee_id>', methods=['GET', 'POST'])
def update_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)

    if request.method == 'POST':
        # Process the form data to update the employee
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.position = request.form['position']
        employee.salary = request.form['salary']
        employee.date_of_joining = request.form['date_of_joining']

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('update_employee.html', employee=employee)


@app.route('/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/api/employees', methods=['GET'])
def api_employees():
    employees = Employee.query.all()
    return jsonify([{
        'employee_id': e.employee_id,
        'name': e.name,
        'email': e.email,
        'position': e.position,
        'salary': e.salary,
        'date_of_joining': str(e.date_of_joining)
    } for e in employees])
