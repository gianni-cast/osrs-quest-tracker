#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Quest, Player, PlayerQuest

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

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
        return make_response(player.to_dict(), 200)
    else:
        return make_response({"error": "Player does not exist"}, 404)

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

if __name__ == '__main__':
    app.run(port=5555, debug=True)

