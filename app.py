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
        "text": "You are an individual from Europe. It's 1262 AC. build your character.",
        "choices": {
            "Continue": "Customization"
        }
    },
    "Customization": {
        "text": "Choose an aspiration.",
        "choices": {
            "Thief": "Thief_Route",
            "Assassin": "Assassin_Route",
            "Soldier": "Soldier_Route",
            "Sage": "Sage_Route",
            "Merchant": "Merchant_Route"
        }
    },
    "Thief_Route": {
        "text": "You start off as a poor peasant. You live close to the woods in the outer city of the kingdom. Your house, as far as you can call it, is a mere shack. Your personal fortune? Nonexistent. You possess a rusty knife and a wicker sack. You own a handful of abilities. Deception, sneak, keen eyes and the ability to pick locks.",
        "choices": {
            "Continue": "Thief_Route_2"
        }
    },
    "Assassin_Route": {
        "text": "You work for a rebel organisation who wants to take over the kingdom. The organisation owns a big hidden camp far way from the city. You spend your free time in a small, but manageable room. Your pay does the job. You possess a special poisonous knife and a mediocre sword. Your abilities: Manipulation, stealth, agility and an understanding of human weak spots.",
        "choices": {
            "Continue": "Assassin_Route_2"
        }
    },
    "Soldier_Route": {
        "text": "You're a soldier of the kingdom. Part of the common infantry. You live in the barracks. The pay is low, but you can work your way to earn more. Your main possessions are a decent sword and a wooden shield. You wear a leather padded vest and a pair of thick boots. The abilities in your favor are strength, endurance, and defense.",
        "choices": {
            "Continue": "Soldier_Route_2"
        }
    },
    "Sage_Route": {
        "text": "You're an individual who started to follow the sage path. You're nowhere near being an excellent one, but the journey is what counts. You travelled to a location far away from everything. You summit a faraway mountain and you built your hut. You own a collection of books and scrolls. Your main activity is writing and studying. You study the stars, your surroundings and the journals made by others far before you. Your abilities are: Wisdom, intuition, virtue and intelligence.",
        "choices": {
            "Continue": "Sage_Route_2"
        }
    },
    "Merchant_Route": {
        "text": "You start off as a beginner merchant. You work for a local merchant guild. Your job is all about bartering, buying and selling. The guild pays you accordingly. You travel a lot throughout the country and you take your rest at local inns. You own a small collection of goods as you spend your own money on them wisely. You furthermore have a reasonable sword sheath. Your abilities are: Commerce, diplomacy and negotiation.",
        "choices": {
            "Continue": "Merchant_Route_2"
        }
    },
    ##################################################

    "Thief_Route_2": {
        "text": "You start off as a poor peasant. You live close to the woods in the outer city of the kingdom. Your house, as far as you can call it, is a mere shack. Your personal fortune? Nonexistent. You possess a rusty knife and a wicker sack. You own a handful of abilities. Deception, sneak, keen eyes and the ability to pick locks.",
        "choices": {
            "Continue": "Thief_Route_3"
        }
    },
    "Assassin_Route_2": {
        "text": "You work for a rebel organisation who wants to take over the kingdom. The organisation owns a big hidden camp far way from the city. You spend your free time in a small, but manageable room. Your pay does the job. You possess a special poisonous knife and a mediocre sword. Your abilities: Manipulation, stealth, agility and an understanding of human weak spots.",
        "choices": {
            "Continue": "Assassin_Route_3"
        }
    },
    "Soldier_Route_2": {
        "text": "You're a soldier of the kingdom. Part of the common infantry. You live in the barracks. The pay is low, but you can work your way to earn more. Your main possessions are a decent sword and a wooden shield. You wear a leather padded vest and a pair of thick boots. The abilities in your favor are strength, endurance, and defense.",
        "choices": {
            "Continue": "Soldier_Route_3"
        }
    },
    "Sage_Route_2": {
        "text": "You're an individual who started to follow the sage path. You're nowhere near being an excellent one, but the journey is what counts. You travelled to a location far away from everything. You summit a faraway mountain and you built your hut. You own a collection of books and scrolls. Your main activity is writing and studying. You study the stars, your surroundings and the journals made by others far before you. Your abilities are: Wisdom, intuition, virtue and intelligence.",
        "choices": {
            "Continue": "Sage_Route_3"
        }
    },
    "Merchant_Route_2": {
        "text": "It's a bright day and you make your way through a foreign town. you pull your wooden cart, filled with sugar, metals and fur, with you. The guild ordered you to sell everything for 20 golden coins which is double the current value. as you pass the people, you reach a crowd of merchants and commoners shouting and yelling. As you mingle in the crowd, people are walking up to you. As you sell your goods, you make your way back to the guild headquarters. Suddenly, a woman runs up to you. You observe her panicking through her facial expressions and her voice. ",
        "choices": {
            "Continue": "Merchant_Route_3"
        }
    }
    ##################################################
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
