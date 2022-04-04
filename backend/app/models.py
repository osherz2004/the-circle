from app import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    nickname = db.Column(db.String(), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    profile_picture_path = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, pwd):
        self.password_hash = bcrypt.generate_password_hash(pwd).decode()

    def __repr__(self):
        return f"<User {self.nickname}"
