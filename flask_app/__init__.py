from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from keys import app_key

def configure():
    load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = app_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

from flask_app import routes