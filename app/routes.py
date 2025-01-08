from flask import render_template, redirect, url_for, flash, request, jsonify
from app import app, db
from app.models import Employee,User
from app.forms import EmployeeForm, LoginForm
from flask_login import login_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()  
    if form.validate_on_submit():  
        # Assuming you have a User model
        print(form.password.data)
        user = User.query.filter_by(email=form.email.data).first()
        # Add password check here
        if user.password == form.password.data:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))  # Redirect to a protected page
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/allEmployee')
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
