from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class Quest(db.Model, SerializerMixin):
    __tablename__ = "quests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)

    player_quests = db.relationship('PlayerQuest', back_populates='quest')

    serialize_rules = ('-player_quests.quest', '-player_quests.player')

    def __repr__(self):
        return f"<Quest {self.name}, {self.description}>"

class Player(db.Model, SerializerMixin):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False)

    player_quests = db.relationship('PlayerQuest', back_populates='player')

    serialize_rules = ('-player_quests.player', '-player_quests.quest')

    @validates('level')
    def validate_level(self, key, value):
        if not (3 <= int(value) <= 126):
            raise ValueError("Player Level must be between 3 and 126")
        return value
    
    def __repr__(self):
        return f"<Player {self.name}, {self.level}>"

class PlayerQuest(db.Model, SerializerMixin):
    __tablename__ = "player_quests"

    id = db.Column(db.Integer, primary_key=True)
    progress = db.Column(db.String(20), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    quest_id = db.Column(db.Integer, db.ForeignKey('quests.id'), nullable=False)

    player = db.relationship('Player', back_populates='player_quests')
    quest = db.relationship('Quest', back_populates='player_quests')
    
    serialize_rules = ('-player', '-quest')

    @validates('progress')
    def validate_progress(self, key, value): 
        if value not in ['Not Started', 'In Progress', 'Completed']:
            raise ValueError("Progress must be: 'Not Started', 'In Progress', or 'Completed'")
        return value 
    
    def __repr__(self):
        return f"<PlayerQuest {self.progress}>"
