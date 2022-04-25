from flask_socketio import emit


class Player:
    def __init__(self, nickname):
        # user = User.query.filter_by(nickname=nickname).first()
        self.nickname = nickname
        # self.description = user.description
        # self.profile_picture_path = user.profile_picture_path
        # self.is_in_game = True


class Game:
    MAX_PLAYERS = 2

    def __init__(self):
        self.players = []
        self.running = False

    def user_exists(self, nickname):
        for user in self.players:
            if user.nickname == nickname:
                return False
        return True

    def get_number_of_players(self):
        return len(self.players)

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

    def get_players(self):
        players = []
        for p in self.players:
            players.append(p.nickname)
        return players

    def start_game(self):
        emit("game:start", broadcast=True)
