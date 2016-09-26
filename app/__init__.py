from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")

app.config.from_object('config')
app.config['SECRET_KEY'] = 'This is not going to the production ever!!!!'

db = SQLAlchemy(app)

api = Api(app)

auth = HTTPBasicAuth()

SCORE_THRESHOLD = 0.1

from app import views, models, restserver
