from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token
from app import db, app, bcrypt, game
from app.models import User
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os


# The function recives a filename (string) and return if it is an image
def valid_picture_filename(filename):
    allowed_extensions = (".jpg", ".jpeg", ".png")
    return os.path.splitext(filename)[-1] in allowed_extensions


# The function recives a filename (string) and returns the path for the file that will be saved (string)
def get_uploaded_file_path(filename):
    return os.path.join(
        "app/",
        app.config["UPLOAD_FOLDER"],
        secure_filename(filename),
    )


class Users(Resource):
    # The function returns a list of the users in the game.
    def get(self):
        users = User.query.filter(User.nickname.in_(game.get_players())).all()

        def map_users(user):
            return {
                "id": user.id,
                "nickname": user.nickname,
                "description": user.description,
                "profile_picture_path": user.profile_picture_path,
            }

        mapped_users = list(map(map_users, users))
        return mapped_users

    # The function creates a new user (when requests to POST /api/users are sent).
    def post(self):
        # Get fields from user request
        nickname = request.form.get("nickname")
        password = request.form.get("password")
        description = request.form.get("description")
        profile_picture = request.files["profile_picture"]

        # Check if all fields exists
        if not nickname or not password or not description or not profile_picture:
            return {"message": "All fields are required."}, 400

        # Check if uploaded profile picture is a picture
        if not valid_picture_filename(profile_picture.filename):
            return {"message": "Profile picture must be an image."}, 400

        profile_picture_path = get_uploaded_file_path(profile_picture.filename)

        # Save profile picture to uploads/
        try:
            profile_picture.save(profile_picture_path)
        except RequestEntityTooLarge:
            return {"message": "Profile picture is too large."}, 500

        # Create the user and save it to the database
        try:
            user = User(
                nickname=nickname,
                password=password,
                description=description,
                profile_picture_path=profile_picture_path[3:],
            )

            db.session.add(user)
            db.session.commit()
        except Exception as error:
            print(error)
            return {"message": "Error occurd while creating the user."}

        return {
            "nickname": nickname,
            "description": description,
            "profile_picture_path": profile_picture_path[3:],
        }, 201


class Login(Resource):
    # The function logs in users to the game (POST /api/login)
    def post(self):
        # Get fields from user request
        data = request.get_json()
        nickname = data["nickname"]
        password = data["password"]

        # Get user from database
        user = User.query.filter_by(nickname=nickname).first()

        # Check if user exists
        if not user:
            return {"message": "Wrong credentials."}, 403

        # Check if password is currect
        if not bcrypt.check_password_hash(user.password_hash, password):
            return {"message": "Wrong credentials."}, 403

        # Sign JWT
        token = create_access_token(user.nickname, "1d")

        return {
            "token": token,
            "nickname": user.nickname,
            "description": user.description,
            "profile_picture_path": user.profile_picture_path,
        }
