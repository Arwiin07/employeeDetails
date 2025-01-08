from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


app = Flask(__name__, template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mysqlserver:Arwiin%40200016@test-mysqlserver.mysql.database.azure.com:3306/employee_db'

# SSL Configuration
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {
        'ssl': {'ca': 'DigiCertGlobalRootCA.crt.pem'}
    }
}
csrf = CSRFProtect(app)  # Enable CSRF protection

app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

login_manager = LoginManager(app)

login_manager.login_view = 'login'

from app import routes