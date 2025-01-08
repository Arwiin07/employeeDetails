
# Employee Management System


This is a Flask-based Employee Management System that allows users to manage employee records. The system provides functionalities for user authentication, adding, updating, viewing, and deleting employee records.


## Features

- User authentication (login and logout)
- Add new employees
- Update existing employee details
- Delete employees
- View the list of all employees
- Unit tests for core functionalities



## Tech Stack

**Backend Framework:** Flask

**Database:** MySql

**Frontend:** HTML and Bootstrap for styling

**Testing:** Python unittest

**Authentication:** Flask-Login

## Prerequisites
Python 3.8 or higher

Virtual environment (optional but recommended)## Installation

Clone the repository:

```bash
git clone https://github.com/Arwiin07/employeeDetails.git

```
Navigate to the project root folder
```bash
cd employeeDetails

```

Set up a virtual environment (optional):
```bash
python -m venv .venv
```
```bash
venv\Scripts\activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## Database Setup(optional)
To set up the database, follow these steps:

- Locate the MySQL script file in the project root folder (e.g., mysqlscript.sql).

- Open your preferred MySQL client (e.g., MySQL Workbench, command line, etc..
- Copy the contents of the schema.sql file.
- Paste the script into the query editor and execute it.
- The database and its schema will be created.
- This script will automatically create the database with the same schema -   used in this project. Ensure that your MySQL server is running and properly configured before executing the script.

## Configure the database connection string:

In the app/ __init__. py file, update the following line to use your local database connection string:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<hostname>/employee_db'
```

## Run Locally With Docker


Locate to root project folder and run this in command prompt

Build the docker file
```cmd
docker build -t my-employee-app .
```
Docker runs in the port 8000
```cmd
docker run -d -p 8000:80 my-employee-app
```
Access the app in your browser at http://localhost:8000.


__Note__: Make sure Docker is installed on your system. If you haven't installed Docker yet, follow the instructions at docker.com for your platform.
## Run Locally (Without Docker)
Run the Employee Management application.

```python
python main.py
```

Access the app in your browser at http://127.0.0.1:5000.
## Contributor

- Arwin

