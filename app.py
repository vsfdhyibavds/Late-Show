from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Episode, Guest, Appearance

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    if episodes:
        print("DEBUG first episode to_dict:", episodes[0].to_dict())
    episodes_list = [episode.to_dict() for episode in episodes]
    import pprint
    pprint.pprint(episodes_list)
    # Manually build JSON string
    json_str = '[' + ','.join([json.dumps({"id": e["id"], "date": e["date"], "number": e["number"]}) for e in episodes_list]) + ']'
    return Response(json_str, mimetype='application/json')

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict(include_appearances=True))
    else:
        return jsonify({"error": "Episode not found"}), 404

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    guests_list = [guest.to_dict() for guest in guests]
    return jsonify(guests_list)

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    if not (1 <= rating <= 5):
        return jsonify({"errors": ["rating must be between 1 and 5"]}), 400

    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)

    if not episode or not guest:
        return jsonify({"errors": ["Invalid episode_id or guest_id"]}), 400

    appearance = Appearance(rating=rating, episode=episode, guest=guest)
    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict(include_episode=True, include_guest=True)), 201

@app.route('/testjson', methods=['GET'])
def test_json():
    test_data = [
        {"id": 1, "name": "Test 1"},
        {"id": 2, "name": "Test 2"}
    ]
    return jsonify(test_data)

if __name__ == '__main__':
    app.run(debug=True)
