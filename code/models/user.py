import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    # three columns into the users table Model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * from users where username=?"
        # result = cursor.execute(query, (username,)) # params has to be in a form of a tuple, (username,) <-- , is added to make it a tuple
        # row = result.fetchone()
        # if row:
        #     # user = cls(row[0], row[1], row[2])
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * from users where id=?"
        # result = cursor.execute(query, (_id,)) # params has to be in a form of a tuple, (username,) <-- , is added to make it a tuple
        # row = result.fetchone()
        # if row:
        #     # user = cls(row[0], row[1], row[2])
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
