import datetime
import uuid

from app import db


class APIKey(db.Model):
    __tablename__ = "keys"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    str = db.Column(db.String)

    def __init__(self):
        self.str = uuid.uuid4().get_hex()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Utterances(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utterance = db.Column(db.String)

    def __init__(self, utterance):
        self.utterance = utterance

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
