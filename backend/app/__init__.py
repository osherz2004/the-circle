from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from flask_socketio import SocketIO
from app.utils import Game

# Initialize flask application
app = Flask(__name__)

# Set config options
app.config.from_object("app.config")

# Application's dependencies
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
api = Api(app)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins="*")
game = Game()
CORS(app)

from app import routes

migrate = Migrate(app, db)
