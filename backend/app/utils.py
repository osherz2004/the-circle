from flask_socketio import emit


class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.is_in_game = True


class Game:
    MAX_PLAYERS = 2

    def __init__(self):
        self.users = []
        self.running = False

    def user_exists(self, nickname):
        for user in self.users:
            if user.nickname == nickname:
                return False
        return True

    def get_number_of_players(self):
        return len(self.users)

    def add_user(self, nickname):
        # Check if the user is already in the game
        if not self.user_exists(nickname):
            return False

        # Adds the user to the game
        user = Player(nickname)
        self.users.append(user)

        # Start game if there are enough players
        if not self.running and len(self.users) == Game.MAX_PLAYERS:
            self.running = True
            self.start_game()

    def start_game(self):
        emit("game:start", broadcast=True)
