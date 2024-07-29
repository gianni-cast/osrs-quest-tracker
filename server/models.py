from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class Quest(db.Model, SerializerMixin):
    __tablename__ = "quests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)

    player_quests = db.relationship('PlayerQuest', back_populates='quest')

    serialize_rules = ('-player_quests.quest', '-player_quests.player')

class Player():
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False)

    player_quests = db.relationship('PlayerQuest', back_populates='player')

    serialize_rules = ('-player_quests.player', '-player_quests.quest')

class PlayerQuest():
    __tablename__ = "player_quests"
