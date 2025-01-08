import unittest
from flask import Flask
from app import create_app, db, User, Employee  # Import your app and models
from flask_login import login_user


class EmployeeManagementTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(
            test_config=True)  # Configure the app for testing
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create a test database
        db.create_all()

        # Create a test user
        self.test_user = User(email='test@example.com', password='password')
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self, email, password):
        return self.client.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        """Helper method to log out a test user."""
        return self.client.get('/logout', follow_redirects=True)

    def test_login(self):
        response = self.login('test@example.com', 'password')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logout', response.data)

    def test_logout(self):
        """Test user logout."""
        self.login('test@example.com', 'password')
        response = self.logout()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_add_employee(self):
        self.login('test@example.com', 'password')
        response = self.client.post('/add_employee', data=dict(
            name='Arwin',
            email='arwin@example.com',
            position='Developer',
            salary=60000,
            date_of_joining='2023-01-01'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Arwin', response.data)

    def test_update_employee(self):
        self.login('test@example.com', 'password')

        # Add an employee
        employee = Employee(name='Surya', email='surya@example.com',
                            position='Developer', salary=60000, date_of_joining='2023-01-01')
        db.session.add(employee)
        db.session.commit()

        response = self.client.post(f'/update_employee/{employee.employee_id}', data=dict(
            name='Sreedhar',
            email='sreedhar@example.com',
            position='Senior Developer',
            salary=80000
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sreedhar', response.data)

    def test_delete_employee(self):
        self.login('test@example.com', 'password')

        # Add an employee
        employee = Employee(name='Karthik', email='karthik@example.com',
                            position='Developer', salary=60000, date_of_joining='2023-01-01')
        db.session.add(employee)
        db.session.commit()

        # Delete the employee
        response = self.client.post(
            f'/delete_employee/{employee.employee_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Karthik', response.data)

    def test_employee_list(self):
        self.login('test@example.com', 'password')

        # Add employees
        db.session.add(Employee(name='Balaji', email='balaji@example.com',
                       position='Manager', salary=80000, date_of_joining='2022-05-15'))
        db.session.add(Employee(name='Sneka', email='sneka@example.com',
                       position='HR', salary=50000, date_of_joining='2021-09-10'))
        db.session.commit()

        # Retrieve the list
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Balaji', response.data)
        self.assertIn(b'Sneka', response.data)


if __name__ == '__main__':
    unittest.main()
