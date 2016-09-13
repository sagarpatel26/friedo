from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__, static_url_path="")

app.config.from_object('config')
db = SQLAlchemy(app)

api = Api(app)

from app import views, models, restserver
