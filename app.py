from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Player state and story
player_state = {
    "inventory": [],
    "abilities": {},
    "current_scene": "start",
}

with open("story.json", "r") as file:
    story = json.load(file)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/scene", methods=["GET"])
def get_scene():
    scene_id = player_state["current_scene"]
    scene = story.get(scene_id, None)
    if scene:
        return jsonify(scene)
    return jsonify({"error": "Scene not found"}), 404

@app.route("/choice", methods=["POST"])
def make_choice():
    global player_state
    data = request.json
    choice = data.get("choice")
    current_scene = player_state["current_scene"]
    if choice in story[current_scene]["choices"]:
        player_state["current_scene"] = story[current_scene]["choices"][choice]
        return jsonify(story[player_state["current_scene"]])
    return jsonify({"error": "Invalid choice"}), 400

@app.route("/save", methods=["POST"])
def save_game():
    with open("save.json", "w") as file:
        json.dump(player_state, file)
    return jsonify({"message": "Game saved!"})

@app.route("/load", methods=["GET"])
def load_game():
    global player_state
    try:
        with open("save.json", "r") as file:
            player_state = json.load(file)
        return jsonify({"message": "Game loaded!", "player_state": player_state})
    except FileNotFoundError:
        return jsonify({"error": "No save found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
