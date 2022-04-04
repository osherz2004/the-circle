from app import app, api
from app.recourse import Users, Login
from flask import render_template, send_from_directory


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/uploads/<file>")
def get_profile_picture(file):
    return send_from_directory("uploads", file)


api.add_resource(Users, "/api/users")

api.add_resource(Login, "/api/login")
