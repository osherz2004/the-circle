from datetime import timedelta

SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
# os.environ.get("SQLALCHEMY_DATABASE_URI")

SQLALCHEMY_TRACK_MODIFICATIONS = False
MAX_CONTENT_LENGTH = 8 * 1024 * 1024
UPLOAD_FOLDER = "uploads/"
JWT_SECRET_KEY = "super-secret-phrase"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
