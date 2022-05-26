from flask_socketio import emit
import asyncio


class Player:
    def __init__(self, nickname):
        # user = User.query.filter_by(nickname=nickname).first()
        self.nickname = nickname
        self.catfish_count = 0
        self.favorite_count = 0
        self.voted = False
        # self.description = user.description
        # self.profile_picture_path = user.profile_picture_path
        # self.is_in_game = True

    # This function returns the precentage of the ratio between catfish_count and favorite_count.
    def get_points(self):
        return self.catfish_count / self.favorite_count * 100


class Game:
    MAX_PLAYERS = 2

    def __init__(self):
        self.players = []
        self.running = False
        self.chat_open = False
        self.chat_messages = []

    # This function returns if a given player [by his nickname (string)] is in the game.
    def user_exists(self, nickname):
        for user in self.players:
            if user.nickname == nickname:
                return False
        return True

    def get_number_of_players(self):
        return len(self.players)

    # This function gets a player's nickname (string) and adds him to the game.
    def add_user(self, nickname):
        # Check if the user is already in the game
        if not self.user_exists(nickname):
            return False

        # Adds the user to the game
        user = Player(nickname)
        self.players.append(user)

        # Start game if there are enough players
        if not self.running and len(self.players) == Game.MAX_PLAYERS:
            self.running = True
            self.start_game()

    # This function returns a list of all the nicknames of the players.
    def get_players(self):
        players = []
        for p in self.players:
            players.append(p.nickname)
        return players

    # This function opens chat for the other players.
    def open_chat(self):
        self.chat_open = True
        emit("game:message", {"message": "Chat rooms are now open."}, broadcast=True)

    # This function starts the game.
    def start_game(self):
        emit("game:start", broadcast=True)
        self.open_chat()

    # This function gets a list of votes and increment the result in the counters of the players.
    def vote(self, vote, nickname):
        # Check if player already voted.
        for player in self.players:
            if player.nickname == nickname:
                if not player.voted:
                    player.voted = True
                else:
                    return

        # Update the vote data in every player
        for v in vote:
            for player in self.players:
                if player.nickname == nickname:
                    player.voted = True
                if player.nickname == v["nickname"]:
                    if v["catfish"]:
                        player.catfish_count += 1
                    if v["favorite"]:
                        player.catfish_count += 1

        # Check if there is a player who didn't vote.
        for p in self.players:
            if not p.voted:
                return

        self.winner()

    # This function returns the player with the most points.
    def winner(self):
        max_player = self.players[0].nickname
        max_points = self.players[0].get_points()
        for player in self.players:
            if max_points < player.get_points():
                max_points = player.get_points()
                max_player = player.nickname

        emit("results", max_player)

        self.running = False
