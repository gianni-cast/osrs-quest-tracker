#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource
from flask_cors import CORS

# Local imports
from config import app, db, api
# Add your model imports
from models import Quest, Player, PlayerQuest

CORS(app)

# Views go here!
@app.route('/')
def index():
    return '<h1>OldSchool Runescape Quest Tracker</h1>'

@app.route('/players', methods=["GET"])
def players_route():
    players = []
    for player in Player.query.all():
        player_dict = {
            "level": player.level,
            "id": player.id,
            "name": player.name,
        }
        players.append(player_dict)
    
    response = make_response(
        players,
        200,
        {"Content-Type": "application/json"}
    )

    return response

@app.route('/players/<int:id>', methods=["GET"])
def get_player(id):
    player = Player.query.get(id)
    if player:
        player_data = {
            "id": player.id,
            "name": player.name,
            "level": player.level,
            "player_quests": [
                {
                    "id": pq.id,
                    "progress": pq.progress,
                    "quest": {
                        "id": pq.quest.id,
                        "name": pq.quest.name,
                        "description": pq.quest.description
                    }
                }
                for pq in player.player_quests
            ]
        }
        response = make_response(player_data)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response({"error": "Player does not exist"})
        response.headers['Content-Type'] = 'application/json'
        return response, 404
    
@app.route('/players', methods=["POST"])
def create_player():
    data = request.get_json()
    name = data.get("name")
    level = data.get("level")

    player = Player(name=name, level=level)

    db.session.add(player)
    db.session.commit()

    quests = Quest.query.all()
    for quest in quests:
        pq = PlayerQuest(player=player, quest=quest, progress="Not Started")
        db.session.add(pq)
    db.session.commit()

    response = make_response(
        player.to_dict(),
        201,
        {"Content-Type": "application/json"}
    )
    
    return response

@app.route('/players/<int:id>', methods=["DELETE"])
def delete_player(id):
    player = Player.query.get(id)

    if player:
        PlayerQuest.query.filter_by(player_id=id).delete()
        db.session.delete(player)
        db.session.commit()

        return make_response(
            {"message": "Player deleted successfully"},
            200,
            {"Content-Type": "application/json"}
        )
    else: 
        return make_response(
            {"error": "Player not found"},
            404,
            {"Content-Type": "application/json"}
        )

@app.route('/players/<int:id>', methods=["PATCH"])
def update_player(id):
    data = request.get_json()

    player = Player.query.get(id)

    if player:
        for key, value, in data.items():
            if hasattr(player, key):
                if key == 'level':
                    value = int(value)
                    if not (3 <= value <= 126):
                        raise ValueError("Player Level must be between 3 and 126")
                setattr(player, key, value)
    
        db.session.commit()

        return make_response(
            player.to_dict(),
            200,
            {"Content-Type": "application/json"}
        )
    
    else:
        return make_response(
            {"error": "Player not found"},
            404,

        )
        
@app.route('/quests', methods=["GET"])
def quests_route():
    quests = []
    for quest in Quest.query.all():
        quest_dict = {
            "description": quest.description,
            "id": quest.id,
            "name": quest.name,
        }
        quests.append(quest_dict)
    
    response = make_response(
        quests,
        200,
        {"Content-Type": "application/json"}
    )

    return response

@app.route('/quests/<int:id>', methods=["GET"])
def get_quest(id):
    quest = Quest.query.get(id)
    if quest:
        return make_response(quest.to_dict(), 200)
    else:
        return make_response({"error": "Quest does not exist"})

@app.route('/quests', methods=["POST"])
def create_quest():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")

    quest = Quest(name=name, description=description)

    db.session.add(quest)
    db.session.commit()

    players = Player.query.all()
    for player in players:
        pq = PlayerQuest(player=player, quest=quest, progress="Not Started")
        db.session.add(pq)
    db.session.commit()

    response = make_response(
        quest.to_dict(),
        201,
        {"Content-Type": "application/json"}
    )

    return response

@app.route('/players/<int:player_id>/quests/<int:quest_id>', methods=["PATCH"])
def update_player_quest_progress(player_id, quest_id):
    data = request.get_json()
    new_progress = data.get('progress')
    
    player_quest = PlayerQuest.query.filter_by(player_id=player_id, quest_id=quest_id).first()

    if player_quest:
        if new_progress not in ['Not Started', 'In Progress', 'Completed']:
            return make_response(
                {"error": "Invalid progress status. Must be 'Not Started', 'In Progress', 'Completed'."},
                400,
            )
    
        player_quest.progress = new_progress

        db.session.commit()

        return make_response(
            player_quest.to_dict(),
            200,
            {"Content-Type": "application/json"}
        )
    
    else:
        return make_response(
            {"error": "PlayerQuest not found"},
            404
        )

if __name__ == '__main__':
    app.run(port=5555, debug=True)

