# rooms_config defines all the rooms in the game_classes. Each key is a room
# name and each value is a dictionary with the name (str) of the room, item
# (dict or None) with the item name and use, and exits (dict) with the cardinal
# directions and name of the rooms they lead to
rooms_config = {
    "bedroom": {
        "name": "bedroom",
        "item": None,
        "exits": {"north": "living room", "east": "kids' room"}
    },
    "living room": {
        "name": "living room",
        "item": {"item_name": "pro camera",
                 "item_use": "document clear proof of the existence of el "
                             "Chupacabras"},
        "exits": {"north": "storage room", "east": "kitchen",
                  "south": "bedroom", "west": "bathroom"}
    },
    "kids' room": {
        "name": "kids' room",
        "item": {"item_name": "goat plushie",
                 "item_use": "distract el Chupacabras"},
        "exits": {"west": "bedroom"}
    },
    "storage room": {
        "name": "storage room",
        "item": {"item_name": "machete",
                 "item_use": "kill el Chupacabras if you have to"},
        "exits": {"east": "backyard", "south": "living room"}
    },
    "kitchen": {
        "name": "kitchen",
        "item": {"item_name": "frying pan",
                 "item_use": "knock out el Chupacabras"},
        "exits": {"north": "garage", "west": "living room"}
    },
    "bathroom": {
        "name": "bathroom",
        "item": {"item_name": "shampoo bottle",
                 "item_use": "blind el Chupacabras"},
        "exits": {"east": "living room"}
    },
    "garage": {
        "name": "garage",
        "item": {"item_name": "rope",
                 "item_use": "tie up el Chupacabras"},
        "exits": {"south": "kitchen"}
    },
    "backyard": {  # Villain room
        "name": "backyard",
        "item": None,
        "exits": {"west": "storage room"}
    }
}
