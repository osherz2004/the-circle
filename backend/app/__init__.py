from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate

# Initialize flask application
app = Flask(__name__)

# Set config options
app.config.from_object("app.config")

# Application's dependencies
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
api = Api(app)
jwt = JWTManager(app)
CORS(app)

from app import routes

migrate = Migrate(app, db)
