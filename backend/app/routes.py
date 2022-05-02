from app import app, api, socketio, game
from app.recourse import Users, Login
from flask import render_template, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_socketio import emit


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/uploads/<file>")
def get_profile_picture(file):
    return send_from_directory("uploads", file)


api.add_resource(Users, "/api/users")

api.add_resource(Login, "/api/login")


@socketio.on("connect")
@jwt_required()
def handle_connect():
    current_user = get_jwt_identity()
    game.add_user(current_user)


@socketio.on("status:get")
@jwt_required()
def handle_get_game_status():
    emit(
        "status:recive",
        {
            "running": game.running,
            "max": game.MAX_PLAYERS,
            "current": game.get_number_of_players(),
        },
        broadcast=True,
    )


@socketio.on("chat:get")
@jwt_required()
def handle_get_chat_messages():
    if not game.chat_open:
        emit(
            "chat:recive",
            [
                {
                    "id": 1,
                    "message": "Chat is closed.",
                    "profile_picture_path": "https://play-lh.googleusercontent.com/ve6ZSaZ3XmNUfusBs4sVKKOvPpJJRETo76_n9W4L3cWt5j09F-M_mobKdvjv2a1-2y0",
                    "player": "Game",
                }
            ],
            broadcast=True,
        )
    else:
        emit(
            "chat:recive",
            game.chat_messages,
            broadcast=True,
        )


@socketio.on("chat:send")
@jwt_required()
def handle_get_chat_messages(message):
    message["id"] = len(game.chat_messages)
    game.chat_messages.append(message)
    emit(
        "chat:recive",
        game.chat_messages,
        broadcast=True,
    )
