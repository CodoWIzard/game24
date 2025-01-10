# Author: Sigma
# License: MIT
# Version: 1.0

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("index.html")


# Story Data
story = {
    "start": {
        "text": "You are in a dark forest. There's a path to the left and one to the right.",
        "choices": {
            "left": "dark_cave",
            "right": "sunny_meadow"
        }
    },
    "dark_cave": {
        "text": "You enter a dark cave. It's cold and you hear dripping water.",
        "choices": {
            "explore": "hidden_treasure",
            "leave": "start"
        }
    },
    "sunny_meadow": {
        "text": "You find yourself in a sunny meadow with flowers all around.",
        "choices": {
            "rest": "happy_ending",
            "return": "start"
        }
    },
    "hidden_treasure": {
        "text": "You found hidden treasure! Congratulations!",
        "choices": {}
    },
    "happy_ending": {
        "text": "You lay down and enjoy the warm sun. The end.",
        "choices": {}
    }
}

# API data
@app.route("/scene", methods=["GET"])
def get_scene():
    scene_id = request.args.get("scene_id", "start")
    scene = story.get(scene_id, None)
    if scene:
        return jsonify(scene)
    return jsonify({"error": "Scene not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
