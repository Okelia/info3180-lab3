from flask import Flask
from flask_mail import Mail
from .config import Config

SECRET_KEY = 'Sup3r$3cretkey'
app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
from app import views