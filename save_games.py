import json
import game_field
import soldier
import screen

data = {
    "key": -1,
    "soldier leg": soldier.soldier_legs,
    "soldier body": soldier.soldier_body,
    "mines location": game_field.mine_matrix_locations,
    "grass location": screen.init_grass_locations
}

def save_game(key, path):
    data["key"] = key
    with open(path, "w") as f:
        json.dump(data, f)

def pull_game(path):
    with open(path, "r") as f:
        return json.load(f)

def update_data(key,path):
    for item in json.load(open(path)):
        if item["key"] == key:
            item.update(data)




