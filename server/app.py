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
        return make_response(player.to_dict(), 200)
    else:
        return make_response({"error": "Player does not exist"}, 404)
    
@app.route('/players', methods=["POST"])
def create_player():
    data = request.get_json()
    name = data.get("name")
    level = data.get("level")

    try:
        player = Player(name=name, level=level)

        db.session.add(player)
        db.session.commit()

        response = make_response(
            player.to_dict(),
            201,
            {"Content-Type": "application/json"}
        )
    
    except:
        response = make_response(
            {"errors": "Incorrect Format"},
            400,
            {"Content-Type": "application/json"}
        )
    
    return response

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

    try:
        quest = Quest(name=name, description=description)

        db.session.add(quest)
        db.session.commit()

        response = make_response(
            quest.to_dict(),
            201,
            {"Content-Type": "application/json"}
        )
    
    except:
        response = make_response(
            {"errors": "Incorrect Format"},
            400,
            {"Content-Type": "application/json"}
        )
    
    return response

# @app.route('/quests', methods=["POST"])
# def create_player():
#     data = request.get_json()
#     name = data.get("name")
#     description = data.get("description")

#     try:
#         quest = Quest(name=name, description=description)

#         db.session.add(quest)
#         db.session.commit()

#         response = make_response(
#             quest.to_dict(),
#             201,
#             {"Content-Type": "application/json"}
#         )
    
#     except ValueError:
#         response = make_response(
#             {"errors": ["validation errors"]},
#             400,
#             {"Content-Type": "application/json"}
#         )
    
#     return response


# @app.route('/players/<int:player_id>/quests/<int:quest_id>', methods=["PATCH"])
# def update_player_quest_progress(player_id, quest_id):
#     data = request.get_json()
#     progress = data.get('progress')
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

